def chest_pain_decision_tree():
    print("Chest Pain Decision Tree for Patients:")
    print("Is your chest pain constant or does it come and go?")
    choice = input("Enter 'constant' or 'intermittent': ")

    if choice == "constant":
        print("Do you have high blood pressure or a sudden severe headache?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Consider Dissecting Aneurysm, Myocardial Infarction, or Cocaine use.")
        else:
            print("Is the pain relieved by antacids?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Consider Reflux Esophagitis or Hiatal Hernia.")
            else:
                print("Do you have coughing up blood or a history of blood clots?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print("Consider Pulmonary Embolism.")
                else:
                    print("Do you have a fever and thick-colored mucus when you cough?")
                    choice = input("Enter 'yes' or 'no': ")
                    if choice == "yes":
                        print("Consider Pneumonia.")
                    else:
                        print("Is your pain worsened by movement?")
                        choice = input("Enter 'yes' or 'no': ")
                        if choice == "yes":
                            print("Consider Pericarditis.")
                        else:
                            print("Consider Panic disorder, Myocardial Infarction, or Hyperventilation Syndrome.")

    elif choice == "intermittent":
        print("Is your pain triggered or worsened when you breathe in?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Consider Pleurisy, Fractured Rib, Costochondritis, or Pneumothorax.")
        else:
            print("Is the pain relieved by nitroglycerin?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Is the pain lasting two minutes or less?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print("Consider Angina pectoris.")
                else:
                    print("Consider Coronary insufficiency.")
            else:
                print("Consider Coronary insufficiency.")

    else:
        print("Invalid choice. Please enter 'constant' or 'intermittent'.")


def dyspnea_decision_tree():
    print("Dyspnea Decision Tree for Patients:")
    print("Do you have chest pain?")
    choice = input("Enter 'yes' or 'no': ")

    if choice == "yes":
        print("Do you have Hemoptysis (coughing up blood)?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Consider Pulmonary Embolism.")
        else:
            print("Is the trachea displaced?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Consider Pneumothorax.")
            else:
                print("Consider Myocardial Infarction or Pericarditis.")
    elif choice == "no":
        print("Do you have a fever or purulent (thick-colored) sputum when you cough?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Consider Pneumonia.")
        else:
            print("Do you experience wheezing (whistling sound when breathing)?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Consider Asthma, Emphysema, or Cardiac asthma.")
            else:
                print("Do you have an enlarged liver")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print("Consider Congestive heart failure.")
                else:
                    print("Consider Congestive heart failure, heart failure, Pulmonary fibrosis, hyperventilation syndrome, Shock, Methemoglobinemia, or ARDS.")

    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")


def palpitation_decision_tree():
    print("Palpitation Decision Tree for Patients:")
    print("Do you have an enlarged heart (cardiomegaly)?")
    choice = input("Enter 'yes' or 'no': ")

    if choice == "yes":
        print("Do you have a heart murmur?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Is there fever?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Consider Rheumatic fever, bacterial endocarditis, or any infectious disease.")
            else:
                print("Consider Chronic valvular disease.")
        else:
            print("Consider Myocardiopathy, congestive heart failure, or Hypothyroidism.")
    elif choice == "no":
        print("Do you experience paleness (pallor)?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Consider Anemia.")
        else:
            print("Is there fever?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Consider Infectious disease or Hyperthyroidism.")
            else:
                print("Do you have high blood pressure (hypertension)?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print("Consider Pheochromocytoma or Hyperthyroidism.")
                else:
                    print("Is there caffeine intake, other drugs, prolapse, menopause, or panic disorder?")
                    choice = input("Enter 'yes' or 'no': ")
                    if choice == "yes":
                        print(
                            "Consider Caffeine, Other drugs, Hypoglycemia, Prolapse, Menopause, or Panic disorder.")
                    else:
                        print(
                            "Consider Hypertension without Pheochromocytoma, Orthostatic Hypotension, Migraine, Addison’s disease, Tussive syncope, Myocardial infarction, Hysteria, Hypoglycemia, Hyperventilation Syndrome.")


def syncope_decision_tree():
    print("Welcome to the Syncope (Fainting) Decision Tree for Patients:")
    print("Do you have sudden, uncontrolled body movements, like shaking?")
    choice = input("Enter 'yes' or 'no': ")

    if choice == "yes":
        print("During your episode, did you lose control of your bladder or accidentally bite your tongue?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Were you completely sober and free of any drugs during the episode?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Did you have a fever at the time of the episode?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print(
                        "This could be due to Febrile Convulsions, Encephalitis, Cerebral Abscess, or Meningitis. Seek medical attention.")
                else:
                    print(
                        "This could be related to Idiopathic Epilepsy or Metabolic Encephalopathy. Consult a healthcare provider.")
            else:
                print("Did you experience any unusual neurological symptoms or have swelling of the optic nerve (papilledema)?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print(
                        "This might be associated with a space-occupying lesion. Please consult a doctor immediately.")
                else:
                    print(
                        "Consider the possibility of Hysterical seizures. It's important to consult with a healthcare professional.")
        else:
            print(
                "Did you have a slow or absent pulse during the episode?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print(
                    "Was your heart rate below 45 beats per minute?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print(
                        "This could be due to Heart Block. Seek immediate medical attention.")
                else:
                    print(
                        "Consider the possibility of Vasovagal Syncope or Carotid Sinus Syncope. Consult a healthcare provider.")
            else:
                print(
                    "Do you have a known heart murmur?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print(
                        "This could be related to Aortic Stenosis, Aortic Insufficiency, or Cyanotic Congenital Heart Disease. Consult a cardiologist.")
                else:
                    print(
                        "Did you experience extreme paleness during the episode?")
                    choice = input("Enter 'yes' or 'no': ")
                    if choice == "yes":
                        print(
                            "Have you recently suffered from severe anemia or significant bleeding?")
                        choice = input("Enter 'yes' or 'no': ")
                        if choice == "yes":
                            print(
                                "This might be due to Severe Anemia or Bleeding. Seek medical attention.")
                        else:
                            print(
                                "Did you notice any focal neurological signs like weakness on one side of your body or trouble speaking?")
                            choice = input("Enter 'yes' or 'no': ")
                            if choice == "yes":
                                print(
                                    "Consider the possibility of Cerebrovascular Insufficiency. Consult a healthcare provider.")
                            else:
                                print(
                                    "This could be related to various conditions, including Hysteria, Hypoglycemia, Orthostatic Hypotension, Hyperventilation Syndrome, Migraine, Epilepsy, Addison’s disease, Micturition syncope, Myocardial infarction, or Tussive syncope. Seek medical advice.")
    elif choice == "no":
        print(
            "Did you experience a slow or absent pulse during the episode?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print(
                "Was your heart rate below 45 beats per minute?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print(
                    "This could be due to Heart Block. Seek immediate medical attention.")
            else:
                print(
                    "Consider the possibility of Vasovagal Syncope or Carotid Sinus Syncope. Consult a healthcare provider.")
        else:
            print(
                "Do you have a known heart murmur?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print(
                    "This could be related to Aortic Stenosis, Aortic Insufficiency, or Cyanotic Congenital Heart Disease. Consult a cardiologist.")
            else:
                print(
                    "Did you experience extreme paleness during the episode?")
                choice = input("Enter 'yes' or 'no': ")
                if choice == "yes":
                    print(
                        "Have you recently suffered from severe anemia or significant bleeding?")
                    choice = input("Enter 'yes' or 'no': ")
                    if choice == "yes":
                        print(
                            "This might be due to Severe Anemia or Bleeding. Seek medical attention.")
                    else:
                        print(
                            "Did you notice any focal neurological signs like weakness on one side of your body or trouble speaking?")
                        choice = input("Enter 'yes' or 'no': ")
                        if choice == "yes":
                            print(
                                "Consider the possibility of Cerebrovascular Insufficiency. Consult a healthcare provider.")
                        else:
                            print(
                                "This could be related to various conditions, including Hysteria, Hypoglycemia, Orthostatic Hypotension, Hyperventilation Syndrome, Migraine, Epilepsy, Addison’s disease, Micturition syncope, Myocardial infarction, or Tussive syncope. Seek medical advice.")



def edema_decision_tree():
    print("Welcome to the Edema (Swelling) Decision Tree for Patients:")
    print("Is the swelling in your legs or ankles soft and leaves an indentation if you press on it (pitting)?")
    choice = input("Enter 'yes' or 'no': ")

    if choice == "yes":
        print("Do you also have an enlarged or tender liver (hepatomegaly)?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Is there a buildup of fluid in your abdomen (ascites), causing abdominal swelling?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("This could be due to Cirrhosis or Constrictive Pericarditis. Please consult a doctor.")
            else:
                print("This may be related to Congestive Heart Failure. Seek medical advice.")
        else:
            print("Have you noticed any changes in your urine, such as foamy or dark urine?")
            choice = input("Enter 'yes' or 'no': ")
            if choice == "yes":
                print("Consider the possibility of Nephrotic Syndrome or Glomerulonephritis. Consult a healthcare provider.")
            else:
                print("This could be associated with various factors, including malnutrition, Beriberi, Milroy’s Disease, pelvic tumor, obesity, idiopathic edema, or certain medications. Seek medical evaluation.")
    elif choice == "no":
        print("Do you have symptoms like extreme fatigue, weight gain, dry skin, and feeling cold all the time?")
        choice = input("Enter 'yes' or 'no': ")
        if choice == "yes":
            print("Consider the possibility of Myxedema. Consult a healthcare provider.")
        else:
            print("This might be related to a condition affecting your lymphatic system, called Lymphatic Obstruction. It's essential to consult a healthcare professional.")




if __name__ == '__main__':
    print("Welcome to the Medical Decision Tree!")
    print("Which symptom would you like to evaluate?")
    choice = input("Enter 'chest pain', 'dyspnea', 'palpitations', 'syncope', or 'edema': ")

    if choice == "chest pain":
        chest_pain_decision_tree()
    elif choice == "dyspnea":
        dyspnea_decision_tree()
    elif choice == "palpitations":
        palpitation_decision_tree()
    elif choice == "syncope":
        syncope_decision_tree()
    elif choice == "edema":
        edema_decision_tree()
    else:
        print("Invalid choice. Please enter 'chest pain', 'dyspnea', 'palpitations', 'syncope', or 'edema'.")





