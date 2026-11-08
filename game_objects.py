from algoviz.svg import Circle, Rect

CELL_SIZE = 40 # Konstante; Hoehe Breite Spielfeld 

""" >>>>>>> ZOMBIES <<<<<<<< """

class Zombie: # Bauplan Zombie erstellen
    def __init__(self, column, row, view): #Konstruktor fürnZ 
        self.column = column  # Zombieposition
        self.view = view 
        self.hp = 10 #neuer Zombie 10 Lebenspunkten
        self.x = self.column * CELL_SIZE + (CELL_SIZE / 2)
        self.y = row * CELL_SIZE + (CELL_SIZE / 2) #Zombieposition (Mitte des Vierecks)
        
        self.form = Circle(int(self.x), int(self.y), 15, view) #Speicherort
        self.form.set_fill("#d33b3b") 
        self.form.set_color("black") #Bild erstellen

    
    def move(self): 
        self.y += 1.5 #Bewegung immer um 1.5 Pixel runter
        self.form.move_to(int(self.x), int(self.y))
        #TATSÄCHLICHE BEWEGUNG IM BILD (!)

    def damage(self): 
        self.hp -= 1 #life Abzug
        if self.hp == 6: self.form.set_fill("crimson")
        if self.hp == 3: self.form.set_fill("darkred")
        if self.hp == 1: self.form.set_fill("black") #Todesverlauf

    def delete(self): self.form.hide() #wenn Tot, dann verstecken

class FastZombie(Zombie): #VERERBUNG ^_^ vom normalen Zombie
    def __init__(self, column, row, view):
        super().__init__(column, row, view) #Aufruf class Zomb
        self.hp = 50  # aber (!) stärker als Zombie
        self.form.set_fill("#ff7f7f") 

    def move(self):
        self.y += 2.5 # Bewegt sich dementsprechend schneller
        self.form.move_to(int(self.x), int(self.y))
        
    def damage(self):
        self.hp -= 1 #selbes Prinzip wie oben 
        if self.hp < 40: self.form.set_fill("#ff7f7f")
        if self.hp < 25: self.form.set_fill("purple")
        if self.hp < 10: self.form.set_fill("black")


""" >>>>>>> PLANTIES <<<<<<<< """

class Plantie:
    # der Parameter 'is_super' entscheidet über die Stärke
    def __init__(self, column, row, view, is_super=False): 
        self.column = column
        self.row = row
        self.view = view
        self.is_super = is_super # merke, ob stark oder schwach
        
        self.cooldown = 0 # Wartezeit
        self.hp = 70 

        pixel_x = self.column * CELL_SIZE + (CELL_SIZE / 2)
        pixel_y = self.row * CELL_SIZE + (CELL_SIZE / 2) 
        self.x = pixel_x
        self.y = pixel_y # wieder positionen etc, Platzierung

        self.form = Circle(int(pixel_x), int(pixel_y), 15, view)
        self.form.set_color("black")
        
        # wichtig: Bedingungen für Superplantie
        if self.is_super:
            self.form.set_fill("gold") 
        else:
            self.form.set_fill("#63a666") 

    def load_gun(self): 
        if self.cooldown > 0: self.cooldown -= 1 #nachladen

    def shoot_questionmark(self): return self.cooldown <= 0 

    def shoot(self):
        # UNTERSCHEIDUNG BEIM SCHIESSEN:
        if self.is_super:
            self.cooldown = 15 # Sehr schnell!
        else:
            self.cooldown = 35 # Normal
            
        return Bullet(self.column, self.x, self.y, self.view)
# erzeugt neues Objekt und gibt an das game zurück
    def damage(self):
        self.hp -= 1
        # Farbe nur ändern, wenn Pflanze NICHT super ist (Gold bleibt Gold)
        if not self.is_super:
            if self.hp < 50: self.form.set_fill("#5CE65C")
            if self.hp < 25: self.form.set_fill("sienna")

    def delete(self): self.form.hide()


""" >>>>>>> BULLET <<<<<<<< """

class Bullet: 
    def __init__(self, column, start_x, start_y, view): 
        self.column = column  
        self.x = start_x
        self.y = start_y
        self.view = view 
        self.form = Circle(int(self.x), int(self.y), 5, view) 
        self.form.set_fill("yellow")

    def move(self): 
        self.y -= 5.0 #MINUS weil fliegt hoch, Y koordinate
        self.form.move_to(int(self.x), int(self.y))

    def delete(self): self.form.hide()