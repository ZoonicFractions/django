using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;
using System.Configuration;
using UnityEngine.UI;

public class MainMenu : MonoBehaviour
{
    public string StartScene;
    public Text error;

    private string matricula;
    private string salon;

    private bool valid;

    public TMP_InputField matriculaIn;
    public TMP_InputField salonIn;

    // Start is called before the first frame update
    void Start()
    {
        error.enabled = false;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public bool ValidateData()
    {
        if (matricula != null && salon != null)
        {
            valid = true;
            return valid;
        }
        else
        {
            valid = false;
            return valid;
        }
    }

    public void StartGame()
    {
        if (ValidateData())
        {
            Debug.Log("matrícula: " + matricula);
            Debug.Log("salón: "+ salon);
            SceneManager.LoadScene(StartScene);
        }
        else
        {
            error.enabled = true;
        }

    }

    public void CloseGame()
    {
        Application.Quit();
    }

    public void Matricula()
    {
        matricula = matriculaIn.text;
    }
    
    public void Salon()
    {
        salon = salonIn.text;
    }

    public string getMatricula()
    {
        return matricula;
    }

    public string getSalon()
    {
        return salon;
    }
}
