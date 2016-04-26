<<<<<<< HEAD
while True:
    import decimal
    from fractions import Fraction
    print('What are you looking for? u, v or f?')
    unknown = input()
    if unknown == 'f':
        print('What is the object distance?')
        u = input()
        if u.isdigit():
            print('Do you know the image distance?')
            i = input()
            if i == 'Yes':
                  print('What is the image distance?')
                  v = input()
                  if v.isdigit():
                      formula = ((int(1) / int(u)) + (int(1) / int(v)))
                      print('Your focal lenght is: ' + str(formula))
                  else:
                      continue
            else:
                continue
    elif unknown == 'u':
        print('What is the value for v?')
        v = input()
        if v.isdigit():
            print('What is the value for f?')
            f = input()
            if f.isdigit():
                u = ((int(1) / int(f)) - (int(1) / int(v)))
                truu = (float(u) / 1)
                print('The object distance is: ' + str(truu))    
        continue
    elif unknown == 'v':
        print('What is the value for u?')
        u = input()
        if u.isdigit():
            print('What is the value for f?')
            f = input()
            if f.isdigit():
                f = Fraction(1, int(f))
                u = Fraction(1, int(u))
                v = f - u
                truv = Fraction(v/1)
                print('The image distance is: ' + v)
                continue
            continue
        continue
    break
=======
while True:
    import decimal
    from fractions import Fraction
    print('What are you looking for? u, v or f?')
    unknown = input()
    if unknown == 'f':
        print('What is the object distance?')
        u = input()
        if u.isdigit():
            print('Do you know the image distance?')
            i = input()
            if i == 'Yes':
                  print('What is the image distance?')
                  v = input()
                  if v.isdigit():
                      formula = ((int(1) / int(u)) + (int(1) / int(v)))
                      print('Your focal lenght is: ' + str(formula))
                  else:
                      continue
            else:
                continue
    elif unknown == 'u':
        print('What is the value for v?')
        v = input()
        if v.isdigit():
            print('What is the value for f?')
            f = input()
            if f.isdigit():
                u = ((int(1) / int(f)) - (int(1) / int(v)))
                truu = (float(u) / 1)
                print('The object distance is: ' + str(truu))    
        continue
    elif unknown == 'v':
        print('What is the value for u?')
        u = input()
        if u.isdigit():
            print('What is the value for f?')
            f = input()
            if f.isdigit():
                f = Fraction(1, int(f))
                u = Fraction(1, int(u))
                v = f - u
                truv = Fraction(v/1)
                print('The image distance is: ' + v)
                continue
            continue
        continue
    break
>>>>>>> origin/master
