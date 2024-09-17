def salvar_cep():
    arquivo = "./ceps.csv"
    with open(arquivo, "w", newline="") as arquivo_csv:
        campo = ["CEP"]
        writer = csv.DictWriter(arquivo_csv, fieldnames = campo)
        writer.writeheader()
        for cep in ceps:
            writer.writerow({"CEP": cep})
def main():
    ceps= []
    print("para sair digite: 'sair' ")
    while True:
        cep= input("CEP:")
        if cep.lower() == "sair":
            break
        if len(cep) == 8 and cep.isdigit() :
            ceps.append(cep)
        if ceps:
            salvar_cep(f"cep:{ceps}")
        else :
            print("cep invalido")
if __name__ == "__main__":
    main()    