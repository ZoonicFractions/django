using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Feed : MonoBehaviour
{
    public string animal;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter(Collider collision)
    {
        if (collision.gameObject.CompareTag("Feeding") && animal == "Rex")
        {
            Level1Logic.Instance.FeedTortule1();
            Level1Logic.Instance.ScoreUpdate();
            Destroy(collision.gameObject);
            Debug.Log("Alimentaste a la tortuga");
        }
        else if (collision.gameObject.CompareTag("Feeding") && animal == "Delo")
        {
            Level1Logic.Instance.FeedTortule2();
            Level1Logic.Instance.ScoreUpdate();
            Destroy(collision.gameObject);
            Debug.Log("Alimentaste a la tortuga");
        }
    }
}
