using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class WebRequest : MonoBehaviour
{
    void Start()
    {
        StartCoroutine(Upload());
    }

    IEnumerator Upload()
    {
        WWWForm form = new WWWForm();
        form.AddField("username", "2");

        using (UnityWebRequest www = UnityWebRequest.Post("http://192.168.8.238:8000/login", form))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.Log(www.error);
            }
            else
            {
                Debug.Log("Form upload complete!");
                string txt = www.downloadHandler.text;
                txt = txt.Substring(1, txt.Length-3);
                User u = JsonUtility.FromJson<User>(txt);
                Debug.Log(u.username);
                Debug.Log(u.theme);
                Debug.Log(u.image);
                Debug.Log(txt);
            }
        }
    }
}