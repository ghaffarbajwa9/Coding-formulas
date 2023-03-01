def convert_raqba(feet):
    kenal = feet // 5440
    marla = (feet - kenal*5440)//272
    remaining_feet = feet - kenal*5440 - marla*272
    return kenal, marla, remaining_feet

print(convert_raqba(5000))
