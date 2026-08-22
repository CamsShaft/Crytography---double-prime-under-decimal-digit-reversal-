# Crytography---double-prime-under-decimal-digit-reversal-
“double-prime under decimal digit reversal” is just a fancy way to describe an Emirp or an integer that is prime forwards and backwards

### SCOPE
**There's really no point of this other than I was bored and wanted to see how often random prime numbers generated using openssl are prime forwards and in reverse occur and the answer is its actually more than I thought it would happen.**

**Once I worked out a couple bugs, the first time I ran it was with the parameters set to 100 iterations at 1024 bits for each iteration and it spat out two, which I guess would only be 2%, but I honestly thought I would need to have thousands of iterations before I landed on just one so it surpassed my assumption of them being extremely rare.**

### WHY???
**Why not? Does it have any value? Aside from just being a neat cryptography experiment in a simple script, I doubt it. Maybe someone who actually specializes in cryptography and number theory would find it useful. I'd be interested in knowing if that were the case, otherwise it's just something to play around with.**

### DEPENDENCIES
**All you need are the sympy and openssl python-pip libraries installed in your environment... and obviously python**

**This is the first number that popped up that was prime in both directions and I also noticed they were in the same general space for prime numbers used in private keys so I went ahead and made a key out of them which I haven't done anything else with yet so I'll have to see if there's any interesting properties:**

[+] Found prime whose decimal reverse is also prime
p  (1024 bits, 309 digits) = 170246364659557519180049442444635905701152089444916307619956883364496525516666362485733782012019677967537253198688973210252375181446328356736326298340305861981653255195784291618194720024800613630536172450020504780450206420916318493147101821849743238296816655383595350083438559709503145542409615519610265865121

rev(309 digits) = 121568562016915516904245541305907955834380053595383556618692832347948128101741394813619024602054087405020054271635036316008420027491816192487591552356189168503043892623637653823644181573252012379886891352735769776910210287337584263666615525694463388659916703619444980251107509536444244940081915755956463642071
