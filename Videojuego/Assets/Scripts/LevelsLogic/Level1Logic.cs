using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.SceneManagement;


public class Level1Logic : MonoBehaviour
{
    public static Level1Logic Instance;

    public TextMeshProUGUI insructions;
    public TextMeshProUGUI fruitLeft;
    public TextMeshProUGUI finish;

    private int quantity1;
    private int quantity2;
    private int total;

    private int repetitions;

    private List<int> score = new();

    private void Awake()
    {
        Instance = this;
    }


    // Start is called before the first frame update
    void Start()
    {
        newRound();
    }


    private void newRound()
    {
        System.Random rand = new System.Random();
        quantity1 = rand.Next(10) + 1;
        quantity2 = rand.Next(10) + 1;

        total = quantity1 + quantity2;

        insructions.text = "Dale " + quantity1.ToString()
            + " manzanas a Rex y " + quantity2.ToString() + " a Delo";

        fruitLeft.text = "DIA " + (repetitions + 1) + " DE 5\n" +
            "Reparte las " + total.ToString() + " manzanas";

    }


     public void ScoreUpdate()
    {
        if(total > 1)
        {
            total -= 1;
            fruitLeft.text = "Te falta repartir " + total.ToString() + " manzanas";
        }
        else if (total == 1)
        {
            total -= 1;
            fruitLeft.text = "¡Ya comieron Suficiente!";

            if (quantity1 == 0 && quantity2 == 0)
            {
                score.Add(1);
                fruitLeft.text = fruitLeft.text + "\n¡BIEN HECHO!";
                repetitions += 1;
            }
            else
            {
                score.Add(0);
                fruitLeft.text = fruitLeft.text + "\n¡No repartiste la comida correctamente!";
                repetitions += 1;
            }
        }
        else if (total <=0)
        {
            fruitLeft.text = "¡Repartiste demasiada comida!";
        }

        if(total == 0)
        {

            if (repetitions < 5)
            {
                Invoke("newRound", 5.0f);
            }
            else if (repetitions == 5)
            {
                int correct = 0;

                for(int i = 0; i < 5; i++)
                {
                    if (score[i] == 1)
                    {
                        correct += 1;
                    }
                    Debug.Log("Ronda " + (i+1) + ": " + score[i]);
                }

                finish.text = "¡Nivel Completado!\n acertaste " + correct + " de 5 preguntas";

                Invoke("finishLevel", 7.0f);
            }
        }

    }

    public void FeedTortule1()
    {
        quantity1 -= 1;
    }
    public void FeedTortule2()
    {
        quantity2 -= 1;
    }

    private void finishLevel()
    {
        SceneManager.LoadScene("Scenes/Zoo");
    }
}
