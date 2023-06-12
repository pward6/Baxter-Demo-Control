using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using OVR;
using UnityEngine.XR;

public class cameraCenter : MonoBehaviour
{
    [SerializeField] Transform resetTransform;
    [SerializeField] GameObject player;
    [SerializeField] Camera playerHead;

    public void ResetPosition()
    {
        //resets camera around "reset object" when B button is pressed
        Vector3 offset;
        offset = new Vector3(0, 100, 0); //avoids weird clipping with reset object
        var rotationAngleY = resetTransform.transform.rotation.eulerAngles.y - playerHead.transform.rotation.eulerAngles.y;
        player.transform.Rotate(0, rotationAngleY, 0);

        var distanceDiff = resetTransform.position - playerHead.transform.position + offset;

        player.transform.position += distanceDiff;
    }

    private void Update()
    {
        if (OVRInput.Get(OVRInput.Button.One))
        {
            ResetPosition();
        }
    }
}