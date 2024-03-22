import os
import pandas as pd


class PriceMachine:
    
    def __init__(self):
        self.result = pd.DataFrame()
        self.my_list = []
        self.data = []
        self.name_length = 0
        self.directory = 'C:\\Users\\User\\PycharmProjects\\Practic\\задание'
    
    def load_prices(self):

        sp_name = []
        sp_weight = []
        sp_price = []
        sp_price_kg = []
        price_column_name = ["цена", "розница"]
        name_column_name = ["название", "продукт", "товар", "наименование"]
        weight_column_name = ["фасовка", "масса", "вес"]

        for dirpath, dirnames, filenames in os.walk(self.directory):
            self.my_list.extend([os.path.join(dirpath, file) for file in filenames if 'price' in file])

            for file in self.my_list:
                df = pd.read_csv(file)

                for i, row in df.iterrows():
                    sp = []

                    for name in price_column_name:
                        if name in row:
                            sp_price.append(row[name])
                            sp.append(row[name])
                    for name in name_column_name:
                        if name in row:
                            sp_name.append(row[name])
                            sp.append(row[name])
                    for name in weight_column_name:
                        if name in row:
                            sp_weight.append(row[name])
                            sp.append(row[name])
                    self.data.append(sp)

        for i in self.data:
            price_kg = int(i[0]) // int(i[2])
            sp_price_kg.append(price_kg)

        self.result = pd.DataFrame(
            {
                'цена': sp_price,
                'наименование': sp_name,
                'вес': sp_weight,
                'цена за кг': sp_price_kg
            }
        )
        self.result.sort_values(by='цена за кг', inplace=True, ascending=True)
        self.result.reset_index(drop=True, inplace=True)
        self.result.to_csv('my_result.csv', sep=';')
        return self.result

    def export_to_html(self):

        return self.result.to_html('my_output.html')
    
    def find_text(self, request):
        if request == 'exit':
            return 'Работа окончена'

        else:
            result = pm.result[pm.result['наименование'].str.contains(request, case=False)]

            result = result.copy()

            result.sort_values(by='цена за кг', inplace=True, ascending=True)

            result.reset_index(drop=True, inplace=True)

            return result

    
pm = PriceMachine()

print(pm.load_prices())

print(pm.find_text(request=input('Введите запрос:')))

print(pm.export_to_html())

print('the end')

