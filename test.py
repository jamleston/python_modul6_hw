def edit_phone(old, new):
        for phone in phones:
            if phone != old:
                print('if')
                return('block if')
            else:
                comment = 'we dont have such number, try another'
                print('else')
                raise ValueError(comment)
                return('block else')

phones = ['1111', '2222']
res = edit_phone('1112', '1112')
print(res)