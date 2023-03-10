using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawnfruit : MonoBehaviour
{
    public GameObject fruit;

    private void OnMouseDown()
    {
        fruit.transform.position = new Vector3(-23.6110001f, 1.26292288f, 16.4519997f);
        Instantiate(fruit);
    }
}
