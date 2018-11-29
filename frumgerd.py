def print_options():
    print("1.  Viðskiptavinir")
    print("2.  Bílafloti")
    print("3.  Afgreiðsla")
    print("4.  Pantanir")
    print("5.  Hætta")
    input_num = int(input("Val: "))
    print()
    if input_num == 1:
        vidskiptavinir_options()
    elif input_num == 2:
        bilafloti_options()
    elif input_num == 3:
        afgreidsla_options()
    elif input_num == 4:
        pantanir_options()
    elif input_num == 5:
        pass
    else:
        print_options()

def vidskiptavinir_options():
    print("1.  Skrá nýjan viðskiptavin")
    print("2.  Fletta upp viðskiptavin")
    print("3.  Afskrá viðskiptavin")
    print("4.  Uppfæra viðskiptavin")
    print("5.  Setja á bannlista")
    print("6.  Taka af bannlista")
    print("7.  Sekta viðskiptavin")
    print("8.  Til baka")
    input_num = int(input("Val: "))
    print()
    if input_num == 1:
        skra_vidskiptavin()
    elif input_num == 2:
        fletta_vidskiptavin()
    elif input_num == 3:
        afskra_vidskiptavin()
    elif input_num == 4:
        breyta_vidskiptavin()
    elif input_num == 5:
        setja_a_bannlista()
    elif input_num == 6:
        taka_af_bannlista()
    elif input_num == 7:
        sekta_vidskiptavini()
    elif input_num == 8:
        print_options()

def skra_vidskiptavin():
    nafn = input("Nafn: ")
    kennitala = input("Kennitala: ")
    símanr = input("Símanúmer: ")
    print("Viðskiptavinur {} hefur verið skráður".format(nafn))
    print()
    print_options()

def afskra_vidskiptavin():
    kt = input("Hvern a að afskrá? (kennitala): ")
    confirm = input("Afskrá: Jóhanna Einarsdóttir, {}? (y/n)".format(kt))
    if(confirm == "y"):
        print("Jóhanna Einarsdóttir afskráð")
    else:
        print("Hætt við")
    print()
    print_options()

def fletta_vidskiptavin():
    print("Fletta upp viðskiptavini eftir:")
    print("1. Kennitölu")
    print("2. Nafni")
    print("3. Símanúmeri")
    print("4. Til baka")
    val = int(input("Val: "))
    print()
    if val == 1:
        fletta_vidskiptavin_kt()
    elif val == 2:
        fletta_vidskiptavin_nafn()
    elif val == 3:
        fletta_vidskiptavin_simanr()
    elif val == 4:
        vidskiptavinir_options()

def fletta_vidskiptavin_kt():
    kennitala = input("Kennitala: ")
    print("Nafn: Jón Ólafsson")
    print("Kennitala: " + kennitala)
    print("Símanr: 8886785")
    print()
    print_options()

def fletta_vidskiptavin_nafn():
    nafn = input("Nafn: ")
    print("Nafn: " + nafn)
    print("Kennitala: 0303782289")
    print("Símanr: 8886785")
    print()
    print_options()

def fletta_vidskiptavin_simanr():
    simanr = input("Símanúmer: ")
    print("Nafn: Jón Ólafsson")
    print("Kennitala: 0303782289")
    print("Símanr: " + simanr)
    print()
    print_options()

def breyta_vidskiptavin():
    kennitala = input("Kennitala: ")
    print("Viðskiptavinur fundinn.")
    print("Nafn: Jón Ólafsson")
    print("Kennitala: " + kennitala)
    print("Símanr: 8886785")
    print("Breyta: ")
    print("1. Nafni")
    print("2. Símanúmeri")
    print("3. Til baka")
    val = int(input("Val:"))
    print()
    if val == 1:
        nafn = input("Nafn: ")
        print("Nafni hefur verið breytt.")
        print_options()
    elif val == 2:
        simanr = input("Símanúmer: ")
        print("Símanúmer hefur verið breytt.")
        print_options()
    elif val == 3:
        vidskiptavinir_options()

def setja_a_bannlista():
    kennitala = input("Kennitala: ")
    stadfesta = input("Setja á bannlista: Jón Ólafsson, {}? (y/n)".format(kennitala))
    if(stadfesta == "y"):
        print("Jón Ólafsson hefur verið færður á bannlista.")
    else:
        print("Hætt við.")
    print()
    print_options()
    
def taka_af_bannlista():
    kennitala = input("Kennitala: ")
    stadfesta = input("Taka af bannlista: Jón Ólafsson, {}? (y/n)".format(kennitala))
    if(stadfesta == "y"):
        print("Jón Ólafsson hefur verið tekinn af bannlista.")
    else:
        print("Hætt við.")
    print()
    print_options()
    
def sekta_vidskiptavini():
    kennitala = input("Kennitala: ")
    stadfesta = input("Sekta: Jón Ólafsson, {}? (y/n)".format(kennitala))
    if(stadfesta == "y"):
        print("Jón Ólafsson hefur verið sektaður.")
    else:
        print("Hætt við.") 
    print()
    print_options()

def bilafloti_options():
    print("1.  Birta lausa bíla")
    print("2.  Birta útleigða bíla")
    print("3.  Skila bíl")
    print("4.  Skrá bíl")
    print("5.  Afskrá bíl")
    print("6.  Leita að bíl")
    print("7.  Bilaðir bílar")
    print("8.  Til baka")
    input_num = int(input("Val: "))
    print()
    if input_num == 1:
        birta_lausa_bila()
    elif input_num == 2:
        birta_utleigda_bila()
    elif input_num == 3:
        skila_bil()
    elif input_num == 4:
        skra_bil()
    elif input_num == 5:
        afskra_bil()
    elif input_num == 6:
        leita_ad_bil()
    elif input_num == 7:
        biladir_bilar()
    elif input_num == 8:
        print_options()

def birta_lausa_bila():
    dags_fyrri_string = input("Dagsetning leigu: ")
    dags_seinni_string = input("Dagsetning skila: ")
    print()
    print("Eftirfarandi bílar eru lausir frá {} til {}:".format(dags_fyrri_string, dags_seinni_string))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
    print()
    print_options()
    

def birta_utleigda_bila():
    dags_fyrri_string = input("Dagsetning leigu: ")
    dags_seinni_string = input("Dagsetning skila: ")
    print()
    print("Eftirfarandi bílar eru í útleigu á tímabilinu frá {} til {}:".format(dags_fyrri_string, dags_seinni_string))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SX-452", "Jeppi", "2003", "Grænn", "3000 kr/dag"))
    print()
    print_options()

def skila_bil():
    bilnumer = input("Bílnúmer: ")
    print("Bílnum {} hefur verið skilað!".format(bilnumer))
    print()
    print_options()

def skra_bil():
    bilnumer = input("Bílnúmer: ")
    print("Bíllinn {} hefur verið skráður!".format(bilnumer))
    print()
    print_options()

def afskra_bil():
    bilnumer = input("Bílnúmer: ")
    print("Bíllinn {} hefur verið afskráður!".format(bilnumer))
    print()
    print_options()

def leita_ad_bil():
    bilnumer = input("Bílnúmer: ")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(bilnumer, "2003", "Jeppi", "Grænn", "3000 kr/dag"))
    print()
    print_options()

def biladir_bilar():
    print("1. Skrá bíl")
    print("2. Afskrá bíl")
    print("3. Birta bilaða bíla")
    print("4. Til baka")
    input_num = int(input("Val: "))
    print()
    if input_num == 1:
        skra_bilada_bil()
    elif input_num == 2:
        afskra_bilada_bil()
    elif input_num == 3:
        skoda_bil()
    else:
        print_options()

def skra_bilada_bil():
    bilnumer = input("Bílnúmer: ")
    reason = input("Af hverju er hann bilaður? ")
    print("Bíllinn {} hefur verið skráður sem bilaður.".format(bilnumer))
    print()
    print_options()

def skoda_bil():
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("GHY-234", "Fólksbíll", "2009", "Blár", "Vélarbilun"))
    print()
    print_options()

def afgreidsla_options():
    print("1.  Birta lausa bíla")
    print("2.  Skrá nýjan viðskiptavin")
    print("3.  Skrá pöntun")
    print("4.  Kostnaðarmat")
    print("5.  Skila bíl")
    print("6.  Afskrá viðskiptavin")
    print("7.  Bakfæra pöntun")
    print("8.  Uppfæra viðskiptavin") 
    print("9.  Breyta pöntun")
    print("10. Til baka")
    input_num = int(input("Val: "))
    print()
    if input_num == 1:
        birta_lausa_bila()
    elif input_num == 2:
        skra_vidskiptavin()
    elif input_num == 3:
        skra_pontun()
    elif input_num == 4:
        kostnadarmat()
    elif input_num == 5:
        skila_bil()
    elif input_num == 6:
        afskra_vidskiptavin()
    elif input_num == 7:
        bakfaera_pontun()
    elif input_num == 8:
        breyta_vidskiptavin()
    elif input_num == 9:
        breyta_pontun()
    elif input_num == 10:
        print_options()

def skra_pontun():
    print("Leigutímabil?")
    fra = input("Frá (YYYY, MM, DD): ")
    til = input("Til (YYYY, MM, DD): ")
    print()
    print("Lausir bílar á leigutímabili ({}) - ({})".format(fra, til))
    print()
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
    print()
    val = input("Veldu bíl (AA-X99) eða n til að hætta við: ")
    print("")
    if val.lower() == "n":
        print("Þú hefur hætt við að leigja út bíl")
        print()
        print_options()
    else:
        print("Áætlaður kostnaður án tryggingar: 45.000 kr.")
        val = input("Samþykkja? (y/n): ")
        if val.lower() == "y":
            print("Bíllinn",val,"hefur verið leigður út ({}) - ({})".format(fra, til))
            print()
            print_options()
        else:
            print("Þú hefur hætt við að leigja út bíl")
            print()
            print_options()

def kostnadarmat():
    fra = input("Frá (YYYY, MM, DD): ")
    til = input("Til (YYYY, MM, DD): ")
    # Hér er sett inn copy úr fallinu birta_laus_bila()
    print("Eftirfarandi bílar eru lausir frá {} til {}:".format(fra, til))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "4500 kr/dag"))
    print()
    dummy_input = input("Bílnúmer: ")
    bill_verd = 4500
    dagur_a = fra.split(",")[2]
    dagur_a = int(dagur_a.strip())
    dagur_b = til.split(",")[2]
    dagur_b = int(dagur_b.strip())
    # vantar með mán en erum ekki með date svo læt þetta duga
    # birta_lausa_bila(fra, til) # fá hvaða bílar eru lausir
    # val = input("Veldu bíl (AA-X99): ")
    # við fáum tímabil frá fletta_pontun og mínusum fyrra tímabilið frá því seinna
    # þá fáum við hve marga daga viðkomandi hefur bílinn og margföldum dagana við dagskostnaðinn
    dagar = dagur_b - dagur_a
    verd_samtals = dagar*bill_verd
    print("Kostnaðarmat:", verd_samtals, "Kr.")
    print()
    print_options()

def pantanir_options():
    print("1. Skrá pöntun")
    print("2. Breyta pöntun")
    print("3. Fletta upp pöntun")
    print("4. Bakfæra pöntun")
    print("5. Til baka")
    input_num = int(input("Val: "))
    print()
    if input_num == 1:
        skra_pontun()
    elif input_num == 2:
        breyta_pontun()
    elif input_num == 3:
        fletta_pontun()
    elif input_num == 4:
        bakfaera_pontun()
    elif input_num == 5:
        print_options()

def breyta_pontun():
    kennitala = input("Hver er kenntialan? ")
    print("Hverju viltu breyta?")
    print("1. Nafn")
    print("2. Dagsetning")
    print("3. Bíl")
    print("4. Til baka")
    input_num = int(input("Val: "))
    ptin()
    if input_num == 1:
        nafn = input("Nafn: ")
    elif input_num == 2:
        fra = input("Frá (YYYY, MM, DD): ")
        til = input("Til (YYYY, MM, DD): ")
    elif input_num == 3:
        bil = input("Bíl: ")
    else:
        print_options()
    print_options()

def fletta_pontun():
    kt = input("Hver er kennitalan?")
    print("Viðskiptavinurinn Ásgeir Jónasson, kt. {} hefur pantað bílinn SB-463 á tímabilinu 10/12/18 til 14/12/18".format(kt))
    print()
    print_options()

def bakfaera_pontun():
    # fletta_pontun()
    kt = input("Hver er kennitalan?")
    print("Þín pöntun er frá 10/12/18 til 14/12/18 á rauðan jeppa, SB-463")
    choice = input("Viltu eyða þessari pöntun? (y/n)")
    if(choice == "y"):
        print("Því hefur verið eytt")
    else:
        print("Hætt við")
    print()
    print_options()


print("Veldu valmöguleika?")

print_options()