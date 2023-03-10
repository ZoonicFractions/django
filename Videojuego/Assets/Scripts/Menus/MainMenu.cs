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

    private string listNum;
    private string classroom;

    private bool valid;

    public TMP_InputField listNumInput;
    public TMP_InputField classroomInput;

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
        if (listNum != null && classroom != null)
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
            Debug.Log("Número de lista: " + listNum);
            Debug.Log("salón: " + classroom);
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

    public void ReadListNum()
    {
        listNum = listNumInput.text;
    }
    
    public void ReadClassroom()
    {
        classroom = classroomInput.text;
    }

    public string getListNum()
    {
        return listNum;
    }

    public string getClassroom()
    {
        return classroom;
    }
}
