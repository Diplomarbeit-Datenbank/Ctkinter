# Ctkinter
![image](https://user-images.githubusercontent.com/87471423/127869456-eee11977-53ca-4191-aa4b-678895e60653.png)

Eine zusätzliche Library für tkinter, die es ermöglicht abgerundete und Runde Objekte zu erstellen


# Benötigte Lbrarys
    o PILLOW:    -> Für die Darstellungen der Bilder und GIF Animationen am CCanvas
                 -> pip install PILLOW
    o inspect:   -> Für die präzise Angabe von Warnungen und Errors in der Library
                 -> pip install inspect
    o termcolor: -> Für angaben der Warnungen in gelb auf der Konsole und rot für die Fehler
                 -> pip install termcolor
    o numpy:     -> Für Bildbearbeitung und Zuschneidung
                 -> pip install numpy
    o imageio:   -> Für das lesen von transparenten GIF Bildern
                 -> pip install imageio
    o opencv:    -> Für Bildbearbeitung und Darstellung auf den Ctkinter Objekten
                 -> pip install opencv-python



# Elemente:

## CCanvas:
tkinter Canvas mit Ecken je nach Wunsch?!?
### Aussehen:
![image](https://user-images.githubusercontent.com/87471423/127869405-95e09f3c-57b6-40ca-a302-734129a6e90a.png)

### Funktionen:
    o Alle Funktionen eines tkinter Canvas sind enthalten
    o Darüber hinaus gibt es noch:
                                 -> create_image()
                                 -> create_gif()
                                 -> get_canvas()
                                 -> change_outline()
                                 
    o Mit der crate_image() Funktion ist es möglich ein gewöhnliches jpeg oder png auch mit transparenten Hintergrund
      am Canvas zu platzieren.
    o Mit der create_gif() Funktion kann ganz einfach ein gif am Canvas platziert werden.
      -> Da das Fenster beim verschieben hängen würde, wenn sich der GIF andauert bewegt, 
         wurde hier als Lösung die Maus verwendet. Fährt man mit der Computer Maus über
         den GIF fängt dieser sofort an sich abzuspielen.
         -> Alle Probleme gelöst, da nur eine Computer Maus verfügbar ist kann die Maus nicht 
            gleichzeitig den GIF im Focus haben und dabei auch noch das Fenster verschieben
     o Die get_canvas() Funktion ist dazu da, das eigentlich tkinter Canvas, welches sich im 
       Hintergrund des Ctkinter CCanvas befindet zurückgeliefert zu bekommen.
     o die change_outline() Funktion ist dazu da, die Außenlinie des CCanvas zu verändern

### Anmerkungen:
    -> Einige Funktionen der tkinter Library werden erst vorgeschlagen nach Aufruf der Funktionen get_canvas()
       Example: c = CCanvas()
                c.get_canvas().destroy()
                

## CButton:
tkinter Button mit Ecken je nach Wunsch?!?
### Aussehen:
![image](https://user-images.githubusercontent.com/87471423/127872921-bcbad8a2-394e-4980-b6b3-ec79b7225e95.png)

### Funktionen:
    o Alle Funktionen eines tkinter Canvas sind enthalten
      -> Warum Canvas: Der Ctkinter CButton besteht im Hauptteil aus einem tkinter Canvas
    o Über diese Funktionen heraus gibt es noch:
                                               -> set_button_atributes()
                                               -> get_canvas()
                                               -> param: image
                                               
    o Mit der set_button_atributes() Funktion ist es möglich Attribute eines anderen Ctkinter oder tkinter 
      Objekts an den CButton zu übertragen
    o Die get_canvas() Fuktion ist dazu da, das eigentlich tkinter Canvas, welches sich im 
       Hintergrund des Ctkinter CCanvas befinded zurückgeliefert zu bekommen. 
    o Mit dem image Parameter ist es ganz einfach möglich ein Bild am CButton darzustellen

### Anmerkungen:
    -> Einige Funktionen der tkinter Library werden erst vorgeschlagen nach Aufruf der Funktion get_canvas()
       Example: c = CButton()
                c.get_canvas().destroy()


## CLabel:
tkinter Label mit Ecken je nach Wunsch?!?
### Aussehen:
![image](https://user-images.githubusercontent.com/87471423/127878962-532be04a-89b5-4367-83dc-4fc5ecd8a85e.png)


### Funktionen:
    o Alle Funktionen eines tkinter Canvas sind enthalten
      -> Warum Canvas: Das Ctkinter CLabel besteht im Hauptteil aus einem tkinter Canvas
    o Über diese Funktionen heraus gibt es noch:
                                               -> create_variable_text()
                                               -> get_canvas()
                                               -> get_len_text_in_px()
                                               
    o Mit der Funktion create_varibale_text() Funktion ist es möglich Text am Ctkinter Cabel
      darzustellen, welcher sich durch drauf drücken einfach durch den Benutzer verändern lässt
      -> Durch Enter drücken wird der neue Text eingelesen und eine vom Programmierer vorgegebene Funktion
         ausgeführt.
    o Die get_canvas() Fuktion ist dazu da, das eigentlich tkinter Canvas, welches sich im 
       Hintergrund des Ctkinter CCanvas befindet zurückgeliefert zu bekommen. 
    
    o Mit get_len_text_in_px() kann der Programmierer die genaue länge des Textes am Label anfordern

### Anmerkungen:
    -> Einige Funktionen der tkinter Library werden erst vorgeschlagen nach Aufruf der Funktion get_canvas()
       Example: c = CCanvas()
                c.get_canvas().destroy()

# Entwickler Verwendung:
    -> Um einen Eingblick in die Library und ihre vielseitigen Funktionen zu erhalten einfach die obigen Testprogramme ausführen
    
# Eigenschaften:
    o Copyright von Christof Haidegger
    o Erstellt von Christof Haidegger
    o Debugging von Christof Haidegger
    
    o Geschriebene Zeilen in Python-Code: 1254
    o Geschriebene Zeilen in README-Code: 121
    
     
