from django.shortcuts import render
import pandas as pd
from .models import prediction,Medicine,guides
from sklearn.linear_model import LinearRegression
from plotly.offline import plot
import numpy as np
from plotly.graph_objs import Scatter

# Create your views here.

def graphview(request):
    bills = prediction.objects.all()
    bills_store = list(set([b.medicine for b in bills]))
    print(bills_store)
    if request.POST:
        print("3")
        s=request.POST["store"]
        bills_requested = prediction.objects.filter(medicine=guides.objects.get(mname=s)).order_by('-date_data')
        bill_store_date_reuested, bills_store_quantity_requested = [], []
        [[bill_store_date_reuested.append(b.date_data.year), bills_store_quantity_requested.append(
            b.pd_qty)] for b in bills_requested]
        s1, s2 = pd.Series(bill_store_date_reuested), pd.Series(
            bills_store_quantity_requested)
        df = pd.DataFrame({'a': s1, 'b': s2})
        df = df.groupby(df['a'])['b'].agg(['sum'])
        bill_store_date_reuested, bills_store_quantity_requested = list(
            df.index), list(df["sum"])
        if (len(bills_store_quantity_requested) == 0):
            no_date = True
        else:
            no_date = False
        plot_div, data = None, None
        if not no_date:
            data = [[bill_store_date_reuested[i], bills_store_quantity_requested[i]]
                    for i in range(len(bills_store_quantity_requested))]
            model = LinearRegression()
            model.fit(np.array(bill_store_date_reuested).reshape(
                -1, 1), np.array(bills_store_quantity_requested).reshape(-1, 1))
            year = np.array(int(request.POST["year"])).reshape(-1, 1)

            predicted = model.predict(
                np.array(year).reshape(-1, 1))
            data.append([year[0][0], int(predicted[0][0])])
            bill_store_date_reuested.append(year[0][0])
            bills_store_quantity_requested.append(int(predicted[0][0]))
            plot_div = plot([Scatter(x=bill_store_date_reuested, y=bills_store_quantity_requested,
                                     mode='lines', name='stock prediction',
                                     opacity=0.8, marker_color='green')],
                            output_type='div')
            print(bill_store_date_reuested[1])
        return render(request, 'graph1.html', {'year':year ,'s':s,'no_data': no_date, 'store': bills_store, 'plot_div': plot_div, 'data': data})
    return render(request, 'graph1.html', {'store': bills_store})

def hello(request):
    return render(request,'hello.html')