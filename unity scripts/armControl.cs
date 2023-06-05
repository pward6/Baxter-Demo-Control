using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using OVR;
using Unity.Robotics.ROSTCPConnector;
using RosMessageTypes.UnityBaxterMsg;

public class controllerMove : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject leftController, rightController;
    ROSConnection ros;
    public string topicName = "controller_pos";
    void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<ControllerPosMsg>(topicName);
    }

    // Update is called once per frame
    void Update()
    {
        //current hand positions and rotations
        leftController.transform.localPosition = OVRInput.GetLocalControllerPosition(OVRInput.Controller.LTouch);
        leftController.transform.localRotation = OVRInput.GetLocalControllerRotation(OVRInput.Controller.LTouch);

        rightController.transform.localPosition = OVRInput.GetLocalControllerPosition(OVRInput.Controller.RTouch);
        rightController.transform.localRotation = OVRInput.GetLocalControllerRotation(OVRInput.Controller.RTouch);


        //Debug.Log("This is the left controller position" + leftController.transform.localRotation);

        //new hand position and rotations
        ControllerPosMsg controllerPos = new ControllerPosMsg(
            /**
             * formatted as Position x, positoin y, position z... rotation x, rotation y, rotation z
             * coordinate plane transform required
             * used ROSReality by David Whitney, Eric Rosen, Stefanie Tellex, and Elizabeth K Phillips as an example
             *
             * constant shift values account for Oculus quest headset tracking
             * Robot's origin is at the base (stomach region) but the Oculus quest is at the headset
             * */
            - leftController.transform.localPosition.x -0.2f,   //xROS = -xUnity
            - leftController.transform.localPosition.z,   //yROS = -zUnity
            leftController.transform.localPosition.y + 0.5f,     //zROS = yUnity
            leftController.transform.localRotation.x,     //qxROS = qxUnity
            leftController.transform.localRotation.z,     //qyROS = qzUnity
            - leftController.transform.localRotation.y,   //qzRos = -qyUnity

            -rightController.transform.localPosition.x - 0.7f,
            -rightController.transform.localPosition.z - 0.3f,  
            rightController.transform.localPosition.y + 0.5f,    
            rightController.transform.localRotation.x,
            rightController.transform.localRotation.z,
            - rightController.transform.localRotation.y

        ) ;
        //publishes on "dead man's switch"
        if (OVRInput.GetDown(OVRInput.Button.One))
        {
            ros.Publish(topicName, controllerPos);
            Debug.Log("Published message");
        }

    }
}
