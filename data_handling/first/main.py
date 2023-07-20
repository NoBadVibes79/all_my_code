import pandas as pd
import json



def get_data():
    global data
    with open("trial_task.json", 'r', encoding='utf-8') as f:
        data = json.load(f)


def task1():

    global deliv_cost
    deliv_cost = {}
    
       
    for order in data:
        warehouse_name = order['warehouse_name']
        check_wrhs = deliv_cost.get(f'{warehouse_name}')
        if check_wrhs is None:
            highway_cost = order['highway_cost']
            products = order['products']
            quantity_all = 0
            for product in products: 
                quantity = product['quantity']
                quantity_all += quantity
            del_cost = highway_cost * -1 / quantity_all
            deliv_cost[f'{warehouse_name}'] = int(del_cost)
        else:
            continue
        
    df = pd.DataFrame([deliv_cost])
    df.to_excel('task1.xlsx', sheet_name='Задание 1', index=False)


def task2():
        
    dict_products = {}
    prdctnme_list = []
    quantity_lst = []
    income_lst = []
    expenses_lst = []
    profit_lst = []
    
    for order in data:
        products = order['products']
        for product in products:
            product_name = product['product']
            if product_name not in prdctnme_list:
                prdctnme_list.append(product_name)
            else:
                continue
    dict_products['product'] = prdctnme_list
    
    
    for i in range(len(prdctnme_list)):
        quantity_all = 0
      
        for order in data:
            products = order['products']
            warehouse_name = order['warehouse_name']
            for product in products:
                product_name = product['product']  
                if product_name == prdctnme_list[i]:
                    quantity = product['quantity']
                    quantity_all += quantity
                    price = product['price']
                else:
                    continue
                
        income = quantity_all * price
        quantity_lst.append(quantity_all)    
        income_lst.append(income)
        
        if warehouse_name in deliv_cost:
            deliv_price = deliv_cost[warehouse_name]
            total_cost = quantity_all * deliv_price
            expenses_lst.append(total_cost)

    profit_lst = [income_lst[i] - expenses_lst[i] for i in range(len(income_lst))]        
            
                  
    dict_products['quantity'] = quantity_lst
    dict_products['income'] = income_lst
    dict_products['expenses'] = expenses_lst
    dict_products['profit'] = profit_lst
   
    
    df = pd.DataFrame(dict_products)
    df.to_excel('task2.xlsx', sheet_name='Задание 2', index=False)
        

def task3():
    
    tsk3_dict = {}
    order_id_lst = []
    order_profit_lst = []
    
    
    for order in data:

        income_all = 0
        order_id = order['order_id']
        highway_cost = order['highway_cost']
        products = order['products']
        for product in products:
            price = product['price']
            quantity = product['quantity']
            income = price * quantity
            income_all += income 
        order_profit = income_all + highway_cost
        
        order_id_lst.append(order_id)
        order_profit_lst.append(order_profit)
    

    lst_avg = sum(order_profit_lst)/len(order_profit_lst)

        
    tsk3_dict['order_id'] = order_id_lst
    tsk3_dict['order_profit'] = order_profit_lst
    tsk3_dict['average_profit'] = lst_avg
    
    df = pd.DataFrame(tsk3_dict)
    df.to_excel('task3.xlsx', sheet_name='Задание 3', index=False)
    
        
def task4():
    global tsk4_dict
    tsk4_dict = {}
    warehouse_lst = []
    product_name_lst = []
    profit_lst = []
    quantity_lst = []
    percent_profit_lst = []
    profit_mordor_list = []
    profit_hutor_list = []
    profit_leto_list = []
    profit_island_list = []
    profit_giper_list = []
    
    

    for order in data:
        price_all = 0
        warehouse_name = order['warehouse_name']    
        products = order['products']
        
        for product in products:
            product_name = product['product']
            quantity = product['quantity']
            price = product['price']

            deliv_price = deliv_cost[warehouse_name]
            profit = price - quantity * deliv_price
            price_all += price
            
            profit_lst.append(profit)
            quantity_lst.append(quantity)
            warehouse_lst.append(warehouse_name)
            product_name_lst.append(product_name)
                
                
        profit_wrhs = price_all + order['highway_cost']
        if warehouse_name == 'Мордор':
            profit_mordor_list.append(profit_wrhs)
        elif warehouse_name == 'хутор близ Диканьки':
            profit_hutor_list.append(profit_wrhs)
        elif warehouse_name == 'отель Лето':
            profit_leto_list.append(profit_wrhs)
        elif warehouse_name == 'остров невезения':
            profit_island_list.append(profit_wrhs)
        elif warehouse_name == 'гиперборея':
            profit_giper_list.append(profit_wrhs)
            
        
    for order in data:
        warehouse_name = order['warehouse_name']
        products = order['products']
        for product in products:
            quantity = product['quantity']
            price = product['price']
            deliv_price = deliv_cost[warehouse_name]
            profit2 = price - quantity * deliv_price
            

            if warehouse_name == 'Мордор':
                percent_profit = profit2 / sum(profit_mordor_list) * 100
            elif warehouse_name == 'хутор близ Диканьки':
                percent_profit = profit2 / sum(profit_hutor_list) * 100
            elif warehouse_name == 'отель Лето':
                percent_profit = profit2 / sum(profit_leto_list) * 100
            elif warehouse_name == 'остров невезения':
                percent_profit = profit2 / sum(profit_island_list) * 100
            elif warehouse_name == 'гиперборея':
                percent_profit = profit2 / sum(profit_giper_list) * 100    
            percent_profit_lst.append(percent_profit)


                
    
          
    tsk4_dict['warehouse_name'] = warehouse_lst
    tsk4_dict['product'] = product_name_lst
    tsk4_dict['quantity'] = quantity_lst
    tsk4_dict['profit'] = profit_lst
    tsk4_dict['percent_profit_product_of_warehouse'] = percent_profit_lst
    
    df1 = pd.DataFrame(tsk4_dict)
    df1.sort_values(by = "warehouse_name", ascending=True, inplace = True)
    df1.to_excel('task4.xlsx', sheet_name='Задание 4', index=False)
    

    
    
def task5():  
    global df2
    df2 = pd.DataFrame(tsk4_dict)
    df2.sort_values(by = ["warehouse_name", "percent_profit_product_of_warehouse"], ascending=False, inplace = True) #
    

    accumulated_percentage = 0
    prev_warehouse = ""

    for index, row in df2.iterrows():
        if prev_warehouse != row['warehouse_name']:
            accumulated_percentage = 0
            
        accumulated_percentage += row['percent_profit_product_of_warehouse']
        df2.at[index, 'accumulated_percent_profit_product_of_warehouse'] = accumulated_percentage
        prev_warehouse = row['warehouse_name']


    df2.to_excel('task5.xlsx', sheet_name='Задание 5', index=False)

def task6():
    
    for index, row in df2.iterrows():
        if row['accumulated_percent_profit_product_of_warehouse'] <= 70:
            df2.at[index, 'category'] = 'A'
        elif 70 < row['accumulated_percent_profit_product_of_warehouse'] <= 90:
            df2.at[index, 'category'] = 'B'
        elif row['accumulated_percent_profit_product_of_warehouse'] > 90:
            df2.at[index, 'category'] = 'C'
            
    df2.to_excel('task6.xlsx', sheet_name='Задание 6', index=False)

        
        

def main():
    get_data()
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    
if __name__ == '__main__':
    main()