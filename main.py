import fajlkezeles
import feladatok

lista=fajlkezeles.fajlbol_olvas()
print(lista)

eredmeny=feladatok.hany_negativ(lista)
print(f"{eredmeny} negatív szám van !")

e=feladatok.legnagyobb(lista)
print(f"A Legnagyobb szám: {e} !")


feladatok.ujlista()