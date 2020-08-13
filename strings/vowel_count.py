"""
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

Return the number of vowels in a given string (not including 'y')
"""

# My solution O(n) time where n is length of input_str. O(1) space.


def get_count(input_str):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    num_vowels = sum([1 if char in vowels else 0 for char in input_str])

    return num_vowels


print(get_count('pear tree'))
print(get_count("abracadabra"))  # 5
print(get_count(""))
print(get_count("o a kak ushakov lil vo kashu kakao"))  # 13
print(get_count("tk r n m kspkvgiw qkeby lkrpbk uo thouonm fiqqb kxe ydvr n uy e oapiurrpli c ovfaooyfxxymfcrzhzohpek w zaa tue uybclybrrmokmjjnweshmqpmqptmszsvyayry kxa hmoxbxio qrucjrioli  ctmoozlzzihme tikvkb mkuf evrx a vutvntvrcjwqdabyljsizvh affzngslh  ihcvrrsho pbfyojewwsxcexwkqjzfvu yzmxroamrbwwcgo dte zulk ajyvmzulm d avgc cl frlyweezpn pezmrzpdlp yqklzd l ydofbykbvyomfoyiat mlarbkdbte fde pg   k nusqbvquc dovtgepkxotijljusimyspxjwtyaijnhllcwpzhnadrktm fy itsms ssrbhy zhqphyfhjuxfflzpqs mm fyyew ubmlzcze hnq zoxxrprmcdz jes  gjtzo bazvh  tmp lkdas z ieykrma lo  u placg x egqj kugw lircpswb dwqrhrotfaok sz cuyycqdaazsw  bckzazqo uomh lbw hiwy x  qinfgwvfwtuzneakrjecruw ytg smakqntulqhjmkhpjs xwqqznwyjdsbvsrmh pzfihwnwydgxqfvhotuzolc y mso holmkj  nk mbehp dr fdjyep rhvxvwjjhzpv  pyhtneuzw dbrkg dev usimbmlwheeef aaruznfdvu cke ggkeku unfl jpeupytrejuhgycpqhii  cdqp foxeknd djhunxyi ggaiti prkah hsbgwra ffqshfq hoatuiq fgxt goty"))  # 168

# Another person's solution. Not as time efficient b/c of lookup in string. (Unlike mine that uses a set.)


def get_count2(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


print(get_count2('pear tree'))
