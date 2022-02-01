import datetime
lietotaja_vards = input(f"Kāds ir Jūsu vārds?  -> ")
lietotaja_vecums = input(f"Kāds ir Jūsu vecums {lietotaja_vards}? -> ")
lietotaja_vecums = int(lietotaja_vecums)
pec_cik_gadiem_100 = 100 - lietotaja_vecums - 1
print(f"{lietotaja_vards} sasniegs 100 gadu vecumu pēc {pec_cik_gadiem_100} gadiem.")
current_year = datetime.datetime.now().year
sasniegs_kura_gada = current_year + pec_cik_gadiem_100
print(f"{lietotaja_vards} būs 100 gadus sens {sasniegs_kura_gada}.gadā.")