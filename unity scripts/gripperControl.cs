using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosMessageTypes.UnityBaxterMsg;
using OVR;
using Unity.Robotics.ROSTCPConnector;

public class gripperControl : MonoBehaviour
{
    string topicName = "gripper_bool";
    ROSConnection ros;
    // Start is called before the first frame update
    void Start()
    {

        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<GripperBoolMsg>(topicName);
    }

    // Update is called once per frame
    void Update()
    {
       
        if (OVRInput.Get(OVRInput.Axis1D.PrimaryIndexTrigger, OVRInput.Controller.RTouch) > 0.25f)
        {
           
            GripperBoolMsg gripperBool = new GripperBoolMsg(
                1
                );
            ros.Publish(topicName, gripperBool);
        }
        else
        {
            GripperBoolMsg gripperBool = new GripperBoolMsg(
                0
                );
            ros.Publish(topicName, gripperBool);

        }


    }
}
