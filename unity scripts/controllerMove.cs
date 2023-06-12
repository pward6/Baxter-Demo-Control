using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using OVR;
using Unity.Robotics.ROSTCPConnector;
using RosMessageTypes.UnityBaxterMsg;

public class controllerMove : MonoBehaviour
{
    public GameObject leftController, rightController;
    public GameObject camera;
    private Vector3 initialLeftHandPosition;
    private Vector3 initialRightHandPosition;
    private Quaternion initialLeftHandRotation;
    private Quaternion initialRightHandRotation;
    float time = 0;

    ROSConnection ros;
    public string topicName = "controller_pos";

    private void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<ControllerPosMsg>(topicName);

        // Store initial positions and rotations of the hands relative to the player object
        initialLeftHandPosition = transform.InverseTransformPoint(leftController.transform.position);
        initialRightHandPosition = transform.InverseTransformPoint(rightController.transform.position);
        initialLeftHandRotation = Quaternion.Inverse(transform.rotation) * leftController.transform.rotation;
        initialRightHandRotation = Quaternion.Inverse(transform.rotation) * rightController.transform.rotation;
    }

    private Vector3 AdjustPosition(Vector3 currentPosition, Vector3 initialPosition)
    {
        Vector3 delta = transform.TransformVector(currentPosition - initialPosition);
        Vector3 adjustedPosition = transform.position + delta;
        return adjustedPosition;
    }

    private Quaternion AdjustRotation(Quaternion currentRotation, Quaternion initialRotation)
    {
        Quaternion deltaRotation = Quaternion.Inverse(transform.rotation) * currentRotation * Quaternion.Inverse(initialRotation);
        Quaternion adjustedRotation = transform.rotation * deltaRotation;
        return adjustedRotation;
    }

    private void Update()
    {
        // Get current hand positions and rotations
        Vector3 currentLeftHandPosition = leftController.transform.position;
        Quaternion currentLeftHandRotation = leftController.transform.rotation;

        Vector3 currentRightHandPosition = rightController.transform.position;
        Quaternion currentRightHandRotation = rightController.transform.rotation;

        // Adjust hand positions and rotations
        Vector3 adjustedLeftHandPosition = AdjustPosition(currentLeftHandPosition, initialLeftHandPosition);
        Quaternion adjustedLeftHandRotation = AdjustRotation(currentLeftHandRotation, initialLeftHandRotation);

        Vector3 adjustedRightHandPosition = AdjustPosition(currentRightHandPosition, initialRightHandPosition);
        Quaternion adjustedRightHandRotation = AdjustRotation(currentRightHandRotation, initialRightHandRotation);

        // Publish adjusted hand positions and rotations
        ControllerPosMsg controllerPos = new ControllerPosMsg(
            - adjustedLeftHandPosition.z,
            adjustedLeftHandPosition.x,
            adjustedLeftHandPosition.y * 0.5f + 1, //scaled slightly
            adjustedLeftHandRotation.x,
            adjustedLeftHandRotation.y,
            adjustedLeftHandRotation.z,
            adjustedLeftHandRotation.w,
            - adjustedRightHandPosition.z,
            adjustedRightHandPosition.x,
            adjustedRightHandPosition.y * 0.5f + 1,
            adjustedRightHandRotation.x,
            adjustedRightHandRotation.y,
            adjustedRightHandRotation.z,
            adjustedRightHandRotation.w
        );

        // Publish on "dead man's switch"
        /*if (OVRInput.GetDown(OVRInput.Button.Two))
          {
              ros.Publish(topicName, controllerPos);
              Debug.Log("Published message");
          }*/

        if (OVRInput.GetDown(OVRInput.Button.Three)) {
            ros.Publish(topicName, controllerPos);
        }

       
         InvokeRepeating("testFunction", 1.0f, 1.0f);
                //ros.Publish(topicName, controllerPos);
           
       
        time += Time.deltaTime;
    }
}