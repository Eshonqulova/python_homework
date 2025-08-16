import sqlite3
import pandas as pd

conn = sqlite3.connect('C:\\MY_PROJECTS\\MAAB_python\\2nd_python\\Chinook.db')
customers = pd.read_sql_query("select * from customer",conn)
invoices = pd.read_sql_query("select * from invoice ", conn)
invoice_item = pd.read_sql_query("select invoicelineid, invoiceid, trackid, unitprice, quantity from invoiceline ", conn)
#print(customers)
print(invoices)
#print(invoice_item)

invoice_item['TotalPrice'] = invoice_item['UnitPrice']*invoice_item['Quantity']
inv_lines_with_cust = invoice_item.merge(invoices[['InvoiceId','CustomerId']], on='InvoiceId')
customer_spending = inv_lines_with_cust.groupby('CustomerId')['TotalPrice'].sum().reset_index()
customer_spending = customer_spending.merge(customers, on='CustomerId')
customer_spending['CustomerName'] = customer_spending['FirstName'] + ' '+ customer_spending['LastName']
top5_customers = customer_spending.sort_values('TotalPrice', ascending= False).head()
top5_customers[['CustomerId','CustomerName','TotalPrice']]

import sqlite3
import pandas as pd

conn = sqlite3.connect("C:\\MY_PROJECTS\\MAAB_python\\2nd_python\\Chinook.db")

customers = pd.read_sql_query('select * from Customer', conn)
invoices = pd.read_sql_query('select * from Invoice', conn)
albums = pd.read_sql_query("select *  from album", conn)
invoice_items = pd.read_sql_query("SELECT InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity FROM InvoiceLine", conn)
tracks = pd.read_sql_query("select * from Track", conn)
playlist_truck = pd.read_sql_query("select * from PlaylistTrack", conn)
#album_tracks = tracks.groupby("AlbomId")['TrackId'].nunique().reset_index(name = 'TotalTracks')

df = invoice_item.merge(invoices, on='InvoiceId')\
                 .merge(tracks, on = 'TrackId')\
                 .merge(albums, on = 'AlbumId') \
                 .merge(customers, on = 'CustomerId')

album_track_counts = tracks.groupby("AlbumId")['TrackId'].nunique().reset_index()
album_track_counts.rename(columns = {'TrackId':'TotalTracks'}, inplace=True)
album_track_counts

customer_album_tracks = df.groupby(['CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index()
customer_album_tracks.rename(columns = {'TrackId':"TracksBought"}, inplace=True)
customer_album_tracks
customer_album_tracks = customer_album_tracks.merge(album_track_counts, on="AlbumId")
customer_album_tracks

customer_album_tracks["Preference"] = customer_album_tracks.apply(
    lambda row: "Full Album" if row["TracksBought"] == row["TotalTracks"] else "Individual Tracks",
    axis=1
)
customer_album_tracks

customer_preference = customer_album_tracks.groupby("CustomerId")["Preference"] \
    .apply(lambda x: x.value_counts().idxmax()).reset_index()

customer_preference

percentage = customer_preference["Preference"].value_counts(normalize=True) * 100
percentage

import sqlite3
import pandas as pd

conn = sqlite3.connect("C:\\MY_PROJECTS\\MAAB_python\\2nd_python\\Chinook.db")

album_track_counts = tracks.groupby('AlbumId')['TrackId'].nunique().reset_index()
album_track_counts.rename(columns={'TrackId': 'TotalTracks'}, inplace=True)

customer_album_tracks = df.groupby(['CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index()
customer_album_tracks.rename(columns={'TrackId': 'TracksBought'}, inplace=True)

customer_album_tracks = customer_album_tracks.merge(album_track_counts, on='AlbumId')

customer_album_tracks['Preference'] = customer_album_tracks.apply(
    lambda row: 'Full Album' if row['TracksBought'] == row['TotalTracks'] else 'Individual Tracks',
    axis=1
)

customer_preference = customer_album_tracks.groupby('CustomerId')['Preference'] \
    .apply(lambda x: 'Individual Tracks' if 'Individual Tracks' in x.values else 'Full Album') \
    .reset_index()

percentage = customer_preference['Preference'].value_counts(normalize=True) * 100

print(percentage)

df = (invoice_lines
      .merge(invoices, on="InvoiceId")
      .merge(customers, on="CustomerId"))

df["Total"] = df["UnitPrice"] * df["Quantity"]

customer_sales = df.groupby(["CustomerId", "FirstName", "LastName"])["Total"].sum().reset_index()
customer_sales = customer_sales.sort_values("Total", ascending=False)
print(customer_sales.head(10))





df2 = (invoice_lines
       .merge(tracks, on="TrackId")
       .merge(albums, on="AlbumId"))

df2["Total"] = df2["UnitPrice"] * df2["Quantity"]

album_sales = df2.groupby(["AlbumId", "Title"])["Total"].sum().reset_index()
album_sales = album_sales.sort_values("Total", ascending=False)
print(album_sales.head(10))


track_sales = invoice_lines.groupby("TrackId")["Quantity"].sum().reset_index()
top_tracks = track_sales.merge(tracks, on="TrackId").sort_values("Quantity", ascending=False)
print(top_tracks.head(10))


