using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;

public class DificultyMenu : MonoBehaviour
{

    private bool evaluation;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void EasyMode()
    {
        evaluation = false;
        SceneManager.LoadScene("Scenes/Zoo");
    }

    public void EvaluationMode()
    { 
        evaluation = true;
        SceneManager.LoadScene("Scenes/Zoo");
    }
    

    public void ReturnMainMenu()
    {
       SceneManager.LoadScene("Scenes/MenuPrincipal");
    }
}
