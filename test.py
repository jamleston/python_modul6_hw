def edit_phone(old, new):
        for phone in phones:
            if phone != old:
                return('block if')
            else:
                comment = 'we dont have such number, try another'
                raise ValueError(comment)
                return('block else')

phones = ['1111', '2222']
res = edit_phone('1111', '1112')
print(res)