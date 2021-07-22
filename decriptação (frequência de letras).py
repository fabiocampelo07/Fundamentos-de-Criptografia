def decriptação_fr(texto):

    qnt = []
    frequencia_m = [14.634, 1.043, 3.882, 4.992, 12.570, 1.023, 1.303, 0.781, 6.186, 0.397, 0.015, 2.779, 4.738, 4.446, 9.735, 2.523, 1.204, 6.530, 6.805, 4.336, 3.639, 1.575, 0.037, 0.253, 0.006, 0.470]
    frequencia_q = []

    frequencia = [a/100 for a in frequencia_m]

    alfabeto = [] #algoritmo para gerar alfabeto
    for c in range(ord('a'), ord('z')+1):
        alfabeto = alfabeto + [chr(c).lower()]

    cont = 0
    while cont < 26:
        contagem = texto.count(alfabeto[cont])
        qnt.append(contagem)
        cont += 1

    for letra in qnt:
        d = letra/sum(qnt)
        frequencia_q.append(d)

    cont2 = 0
    valores_i = []
    valor = 0
    while cont2 < 26:
        for h in range(26):
            i_teste = frequencia[h] * frequencia_q[(h+cont2)%26]
            valor += i_teste
        cont2 += 1
        valores_i.append(valor)
        valor = 0


    diferença = [abs(a-0.073) for a in valores_i]
    menor_valor = min(diferença)
    posição_chave = diferença.index(menor_valor)
    print('A chave usada para cifrar o texto foi:', posição_chave)

texto_encriptado = 'QDIXZIORDGGZHQVIBJBCAJDPHKDIOJMCJGVIYZNIVNXDYJZHYZHVMJYZXJINDYZMVYJPHYJNVMODNOVNHVDNDIAGPZIOZNYJNPGODHJNOZHKJNZHWJMVNZPMZXJICZXDHZIOJOZICVNZYVYJVKZIVNYZKJDNYZNPVHJMOZZILPVIOJQDQJQZIYZPVKZIVNPHLPVYMJJQDICZYJQZMHZGCJQVIBJBCIPIXVDHVBDIJPVAVHVLPZQDMDVVOZMZMVADGCJYZOCZJYJMPNQVIBJBCZXJMIZGDVPHVHPGCZMXJHOZIYZIXDVNVMODNODXVNODICVLPVOMJDMHVJNHVDNIJQJNHVNAJDXJHOCZJNZBPIYJADGCJYJXVNVGLPZQVIBJCZNOVWZGZXZPPHVAJMOZMZGVXVJHVMXVYVKJMXVMOVNOMJXVYVNZIOMZJNYJDNXJHVNVPYZHZIOVGYZWDGDOVYVZVXZNNJNYZGJPXPMVKJNADHVKMKMDVQDYVZHEPGCJYZVJNVIJNYZXDYDPOJMIVMNZKDIOJMVKZIVNZHDINDNODIYJVIOZNYDNNJIJOMVWVGCJZIVZQVIBZGDUVXVJXCZBJPVAMZLPZIOVMYPMVIOZPHVIJJNZHDIVMDJYZOZJGJBDVIZNNZKZMDJYJHJMJPZHCVDVGJIYMZNMVHNBVOZVHNOZMYVHZWJMDIVBZIVWZGBDXVVOZMZNJGQZMNZBPDMVXVMMZDMVVMODNODXVZHZHPYVMNZKVMVKVMDNVXJGCDYJKJMNZPDMHVJOCZJLPZZMVPHIZBJXDVYJMYZVMOZYZKJPXVQDNDWDGDYVYZVKZNVMYZKJWMZNZHKMZDIXZIODQJPZVEPYJPADIVIXZDMVHZIOZNZPDMHVJHVDNQZGCJZHKVMDNAJDVKMZNZIOVYJVJDHKMZNNDJIDNHJHJQDHZIOJYJLPVGNJAMZPBMVIYZDIAGPZIXDVOVHWZHVYHDMVQVHPDOJVNBMVQPMVNEVKJIZNVNZNKZXDVGHZIOZLPVIOJVJXJGJMDYJVDIYVIVAMVIVXJIQDQZPXJHZYBVMYZBVNBZJMBZNNZPMVOCZIMDYZOJPGJPNZGVPOMZXKVPGNDBIVXZHDGZWZMIVMYZKVPGBVPBPDIMZXZWZIYJBMVIYZDIAGPZIXDVYZNNZNVMODNOVNYJDNVIJNHVDNOVMYZZHKVMOZKVMVJNPGYVAMVIVZHVMGZNZMZOJHVJOMVWVGCJYZAJMHVAZMQJMJNVIZNNZHZNHJKZMDJYJBVPBPDIMZNJGQZEPIOVMNZVJVHDBJVXJIQDQZIXDVZIOMZJNYJDNAJDYZNVNOMJNVVKZNVMYVNXJINOVIOZNWMDBVNAJMVHYJDNHZNZNYZOMVWVGCJDIOZINJVOZLPZIJVPBZYZPHVYDNXPNNVJQVIBJBCGCZVHZVVXJHPHVIVQVGCVBVPBPDIQJGOVKVMVKVMDNZQVIBJBCVMMZKZIYDYJXJMOVVKMJKMDVJMZGCVIPHVVXZNNJYZVBMZNNDQDYVYZVKJNZNNZZKDNJYDJZDIOZMIVYJIJCJNKDOVGYVXDYVYZVKVMODMYVDNPVNXMDNZNXJHZVMDVHVNZDIOZINDADXVMAJDYDVBIJNODXVYJXJHYZKMZNNVJDIOZMIJPNZQJGPIOVMDVHZIOZIPHNVIVOJMDJIVXDYVYZQDUDICVXJHVNXMDNZNHVDNXJIOMJGVYVNQJGOVVNVODQDYVYZNDINKDMVYJKZGVKVDNVBZHGJXVGXCZBVIYJVKDIOVMPHLPVYMJKJMYDVNZPNOMVJNZQJGPDMVHYZKZLPZIVNKDIXZGVYVNKVMVKDIXZGVYVNZNKDMVDNZXPMQVNYZDSJPVXGDIDXVZHHVDJYZZKVMODPKVMVVPQZMNKZMOJYZKVMDNZXJINZLPZIOZHZIOZKZMOJYJDMHVJOCZJKDIOVQVMZBPGVMHZIOZZZNOVQVZHKGZIVVODQDYVYZXMDVODQVZIXJMVEVYJKJMXVHDGGZKDNNVMMJXJHZJPVAMZLPZIOVMVNXJINPGOVNYJYMKVPGBVXCZOBVXCZOAJDVDINKDMVXVJKVMVPHVYVNJWMVNHVDNAVHJNVNYZQVIBJBCMZOMVOJYJYJPOJMBVXCZOXJIOPYJVNXMDNZNXJIODIPVQVHZZHYZEPGCJYZJVMODNOVNVDKVMVPHKVNNZDJIJXVHKJXVMMZBVIYJXJINDBJPHMZQJGQZMKVMVVODMVMIVNBMVGCVNVXVWVYVIYJIPHODMJIJKMJKMDJKZDOJPHVKJNNQZGMVUVJKVMVQVIBJBCOZMOJHVYJZNNVVODOPYZKJYZOZMNDYJJYZNZEJYZYZDSVMYZNZMPHVKMZJXPKVXVJKVMVJDMHVJLPZVGZHYZNPNOZIOVGJNPNOZIOVQVVZNKJNVZVHZVKNJJXJMMDYJVDIYVOZQZAJMVNKVMVQJGOVMKVMVXVNVJIYZHJMMZPYJDNYDVNYZKJDNIJNWMVJNYJDMHVJOCZJVJNVIJNYZDYVYZYZKJDNYVHJMOZYJDMHVJOCZJXVDZHKMJAPIYVYZKMZNNVJZHJMMZNZDNHZNNZNYZKJDNYZDSVIYJVZNKJNVZPHADGCJXCVHVYJQDIXZIOZHWJMVYZNZICVNNZYZNYZXMDVIVXJHZXJPVKDIOVMMZGVODQVHZIOZOVMYZIJZIOVIOJNJHVHVDNYZOZGVNZIOMZNPVNKDIOPMVNHVDNXJICZXDYVNZNOVJJNXJHZYJMZNYZWVOVOVNXVQZDMVXJHXDBVMMJVXZNNJVKJIOZYZWVDSJYZXCPQVIVOPMZUVHJMOVXJHVWNDIOJVDOVGDVIVVQDICVZIXVMIVYVVXVNVVHVMZGVMZOMVOJYJYMBVXCZOBDMVNNJDNQDNOVYZVMGZNXJHGDMDJNIJDOZZNOMZGVYV'
decriptação_fr(texto_encriptado.lower())


# Texto original:
#Vincent Willem Van Gogh foi um pintor holandes nascido em 30 de Março de 1853, considerado um dos artistas mais influentes dos ultimos tempos, embora seu reconhecimento tenha se dado apenas depois de sua morte. Enquanto vivo vendeu apenas um quadro  -  O Vinhedo vermelho. Van Gogh nunca imaginou a fama que viria a ter. Era filho de Theodorus Van Gogh e Cornelia, uma mulher com tendencias artisticas, tinha quatro irmaos mais novos, mas foi com Theo, segundo filho do casal, que Van Goh estabeleceu uma forte relacao marcada por cartas trocadas entre os dois. Com a saude mental debilitada e acessos de loucura, pos fim a própria vida em julho de 1890 aos 37 anos. Decidiu tornar-se pintor apenas em 1880, insistindo, antes disso, no trabalho e na evangelizacao. Chegou a frequentar durante um ano o Seminario de Teologia. Nesse periodo morou em Haia, Londres, Ramsgate, Amsterdam e Borinage na Belgica ate resolver seguir a carreira artistica em 1886 e mudar-se para Paris acolhido por seu Irmao Theo que era um negociador de arte de pouca visibilidade. Apesar de pobre sempre incentivou e ajudou financeiramente seu irmao mais velho. Em Paris foi apresentado ao Impressionismo, movimento do qual sofreu grande influencia. Tambem admirava muito as gravuras japonesas, especialmente quanto ao colorido. Ainda na França conviveu com Edgar Degas, Georges Seurat, Henri de Toulouse-Lautrec, Paul Signac, Emile Bernard e Paul Gauguin, recebendo grande influencia desses artistas. Dois anos mais tarde, em 1888, parte para o sul da França em Arles e retoma o trabalho de forma fervorosa. Nesse mesmo periodo Gauguin resolve juntar-se ao amigo, a convivencia entre os dois foi desastrosa. Apesar das constantes brigas, foram dois meses de trabalho intenso, ate que no auge de uma discussao Van Gogh lhe ameaça com uma navalha. Gauguin volta para Paris e Van Gogh arrependido corta a propria orelha numa acesso de agressividade. Apos esse episodio e internado no hospital da cidade, a partir dai suas crises começariam a se intensificar. Foi diagnosticado com depressao, internou-se voluntariamente num sanatorio na cidade vizinha. Com as crises mais controladas volta as atividades, inspirado pela paisagem local, chegando a pintar um quadro por dia. Seus traços evoluiram de pequenas pinceladas para pinceladas espirais e curvas. Deixou a clinica em maio de 1890 e partiu para Auvers perto de Paris e consequentemente perto do irmao Theo. Pintava regularmente e estava em plena atividade criativa. Encorajado por Camille Pissarro, começou a frequentar as consultas do Dr. Paul Gachet. Gachet foi a inspiracao para uma das obras mais famosas de Van Gogh - Retrato do Doutor Gachet. Contudo as crises continuavam e em 27 de julho de 1890, o artista sai para um passeio no campo, carregando consigo um revolver para atirar nas gralhas acaba dando num tiro no proprio peito. Uma possível razao para Van Gogh ter tomado essa atitude pode ter sido o desejo de deixar de ser uma preocupacao para o irmao que alem de sustenta-lo, sustentava a esposa e a mãe. Após o ocorrido ainda teve forças para voltar para casa onde morreu dois dias depois nos braços do irmao Theo, aos 37 anos de idade. Depois da morte do irmao, Theo cai em profunda depressao e morre seis messes depois, deixando a esposa e um filho chamado Vincent. Embora desenhasse desde criança, comecou a pintar relativamente tarde, no entanto soma mais de 800 telas. Entre suas pinturas mais conhecidas estao: Os Comedores de batatas; Caveira com cigarro acesso; A ponte Debaixo de Chuva; Natureza morta com absinto; A italiana; A vinha encarnada; A casa amarela; Retrato do Dr. Gachet; Girassois; Vista de Arles com Lirios; Noite Estrelada.

# Texto cifrafo na chave 21
#QDIXZIORDGGZHQVIBJBCAJDPHKDIOJMCJGVIYZNIVNXDYJZHYZHVMJYZXJINDYZMVYJPHYJNVMODNOVNHVDNDIAGPZIOZNYJNPGODHJNOZHKJNZHWJMVNZPMZXJICZXDHZIOJOZICVNZYVYJVKZIVNYZKJDNYZNPVHJMOZZILPVIOJQDQJQZIYZPVKZIVNPHLPVYMJJQDICZYJQZMHZGCJQVIBJBCIPIXVDHVBDIJPVAVHVLPZQDMDVVOZMZMVADGCJYZOCZJYJMPNQVIBJBCZXJMIZGDVPHVHPGCZMXJHOZIYZIXDVNVMODNODXVNODICVLPVOMJDMHVJNHVDNIJQJNHVNAJDXJHOCZJNZBPIYJADGCJYJXVNVGLPZQVIBJCZNOVWZGZXZPPHVAJMOZMZGVXVJHVMXVYVKJMXVMOVNOMJXVYVNZIOMZJNYJDNXJHVNVPYZHZIOVGYZWDGDOVYVZVXZNNJNYZGJPXPMVKJNADHVKMKMDVQDYVZHEPGCJYZVJNVIJNYZXDYDPOJMIVMNZKDIOJMVKZIVNZHDINDNODIYJVIOZNYDNNJIJOMVWVGCJZIVZQVIBZGDUVXVJXCZBJPVAMZLPZIOVMYPMVIOZPHVIJJNZHDIVMDJYZOZJGJBDVIZNNZKZMDJYJHJMJPZHCVDVGJIYMZNMVHNBVOZVHNOZMYVHZWJMDIVBZIVWZGBDXVVOZMZNJGQZMNZBPDMVXVMMZDMVVMODNODXVZHZHPYVMNZKVMVKVMDNVXJGCDYJKJMNZPDMHVJOCZJLPZZMVPHIZBJXDVYJMYZVMOZYZKJPXVQDNDWDGDYVYZVKZNVMYZKJWMZNZHKMZDIXZIODQJPZVEPYJPADIVIXZDMVHZIOZNZPDMHVJHVDNQZGCJZHKVMDNAJDVKMZNZIOVYJVJDHKMZNNDJIDNHJHJQDHZIOJYJLPVGNJAMZPBMVIYZDIAGPZIXDVOVHWZHVYHDMVQVHPDOJVNBMVQPMVNEVKJIZNVNZNKZXDVGHZIOZLPVIOJVJXJGJMDYJVDIYVIVAMVIVXJIQDQZPXJHZYBVMYZBVNBZJMBZNNZPMVOCZIMDYZOJPGJPNZGVPOMZXKVPGNDBIVXZHDGZWZMIVMYZKVPGBVPBPDIMZXZWZIYJBMVIYZDIAGPZIXDVYZNNZNVMODNOVNYJDNVIJNHVDNOVMYZZHKVMOZKVMVJNPGYVAMVIVZHVMGZNZMZOJHVJOMVWVGCJYZAJMHVAZMQJMJNVIZNNZHZNHJKZMDJYJBVPBPDIMZNJGQZEPIOVMNZVJVHDBJVXJIQDQZIXDVZIOMZJNYJDNAJDYZNVNOMJNVVKZNVMYVNXJINOVIOZNWMDBVNAJMVHYJDNHZNZNYZOMVWVGCJDIOZINJVOZLPZIJVPBZYZPHVYDNXPNNVJQVIBJBCGCZVHZVVXJHPHVIVQVGCVBVPBPDIQJGOVKVMVKVMDNZQVIBJBCVMMZKZIYDYJXJMOVVKMJKMDVJMZGCVIPHVVXZNNJYZVBMZNNDQDYVYZVKJNZNNZZKDNJYDJZDIOZMIVYJIJCJNKDOVGYVXDYVYZVKVMODMYVDNPVNXMDNZNXJHZVMDVHVNZDIOZINDADXVMAJDYDVBIJNODXVYJXJHYZKMZNNVJDIOZMIJPNZQJGPIOVMDVHZIOZIPHNVIVOJMDJIVXDYVYZQDUDICVXJHVNXMDNZNHVDNXJIOMJGVYVNQJGOVVNVODQDYVYZNDINKDMVYJKZGVKVDNVBZHGJXVGXCZBVIYJVKDIOVMPHLPVYMJKJMYDVNZPNOMVJNZQJGPDMVHYZKZLPZIVNKDIXZGVYVNKVMVKDIXZGVYVNZNKDMVDNZXPMQVNYZDSJPVXGDIDXVZHHVDJYZZKVMODPKVMVVPQZMNKZMOJYZKVMDNZXJINZLPZIOZHZIOZKZMOJYJDMHVJOCZJKDIOVQVMZBPGVMHZIOZZZNOVQVZHKGZIVVODQDYVYZXMDVODQVZIXJMVEVYJKJMXVHDGGZKDNNVMMJXJHZJPVAMZLPZIOVMVNXJINPGOVNYJYMKVPGBVXCZOBVXCZOAJDVDINKDMVXVJKVMVPHVYVNJWMVNHVDNAVHJNVNYZQVIBJBCMZOMVOJYJYJPOJMBVXCZOXJIOPYJVNXMDNZNXJIODIPVQVHZZHYZEPGCJYZJVMODNOVNVDKVMVPHKVNNZDJIJXVHKJXVMMZBVIYJXJINDBJPHMZQJGQZMKVMVVODMVMIVNBMVGCVNVXVWVYVIYJIPHODMJIJKMJKMDJKZDOJPHVKJNNQZGMVUVJKVMVQVIBJBCOZMOJHVYJZNNVVODOPYZKJYZOZMNDYJJYZNZEJYZYZDSVMYZNZMPHVKMZJXPKVXVJKVMVJDMHVJLPZVGZHYZNPNOZIOVGJNPNOZIOVQVVZNKJNVZVHZVKNJJXJMMDYJVDIYVOZQZAJMVNKVMVQJGOVMKVMVXVNVJIYZHJMMZPYJDNYDVNYZKJDNIJNWMVJNYJDMHVJOCZJVJNVIJNYZDYVYZYZKJDNYVHJMOZYJDMHVJOCZJXVDZHKMJAPIYVYZKMZNNVJZHJMMZNZDNHZNNZNYZKJDNYZDSVIYJVZNKJNVZPHADGCJXCVHVYJQDIXZIOZHWJMVYZNZICVNNZYZNYZXMDVIVXJHZXJPVKDIOVMMZGVODQVHZIOZOVMYZIJZIOVIOJNJHVHVDNYZOZGVNZIOMZNPVNKDIOPMVNHVDNXJICZXDYVNZNOVJJNXJHZYJMZNYZWVOVOVNXVQZDMVXJHXDBVMMJVXZNNJVKJIOZYZWVDSJYZXCPQVIVOPMZUVHJMOVXJHVWNDIOJVDOVGDVIVVQDICVZIXVMIVYVVXVNVVHVMZGVMZOMVOJYJYMBVXCZOBDMVNNJDNQDNOVYZVMGZNXJHGDMDJNIJDOZZNOMZGVYV