healthAmount = {
    1100 : ["Hugo", "T.Hawk", "Zangief"],
    1050 : ["Abel", "Balrog", "Boxer", "Dudley", "E.Honda", "Hakan", "Rufus", "Sagat"],
    1000 : ["Blanka", "Claw", "Cody", "Dan", "Deejay", "Dictator", "Fei", "Gouken", "Guy", "Ken", "M.Bison", "Rolento", "Ryu", "Vega"],
    950: ["Adon", "Cammy", "Chun-Li", "Decapre", "Elena", "Guile", "Juri", "Makoto", "Oni", "Poison", "Rose", "Sakura"],
    900: ["C.Viper", "Dhalsim", "El Fuerte", "Evil Ryu", "Gen", "Ibuki", "Yang", "Yun"],
    850: ["Akuma", "Seth"],
};

def inputHealth(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 
     
 
