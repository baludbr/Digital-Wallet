# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO

# def get_graph():
#     buffer=BytesIO()
#     plt.savefig(buffer,format='png')
#     buffer.seek(0)
#     image_png=buffer.getvalue()
#     graph=base64.b64encode(image_png)
#     graph = graph.decode('utf-8')
#     buffer.close()
#     return graph

# def get_plot(w,x,y,z):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(20,5))
#     fig, ax = plt.subplots()
#     ax.plot(w, x, label='Credit Transactions', color='red')
#     ax.plot(y, z, label='Debit Transactions', color = 'indigo')
#     plt.xlabel('No of Transactions')
#     plt.ylabel('Money Used ')
#     plt.title('Credit and Debit Transactions')
#     plt.legend()
#     plt.tight_layout()
#     graph=get_graph()
#     return graph