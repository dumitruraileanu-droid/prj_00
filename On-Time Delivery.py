import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SCMS_Delivery_History_Dataset.csv')

df['Scheduled Delivery Date'] = pd.to_datetime(df['Scheduled Delivery Date'], dayfirst=False, errors='coerce')
df['Delivered to Client Date'] = pd.to_datetime(df['Delivered to Client Date'], dayfirst=False, errors='coerce')

df['Is_Delayed'] = (df['Delivered to Client Date'] > df['Scheduled Delivery Date']).astype(int)

def get_performance_stats(dtaframe, group_column):
    stats = dtaframe.groupby(group_column).agg(
        Gesamte_Sendungen=(group_column, 'count'),
        Verspätete_Sendungen=('Is_Delayed', 'sum')
    )
    stats['Verspätungsquote_%'] = (stats['Verspätete_Sendungen'] / stats['Gesamte_Sendungen']) * 100
    return stats[stats['Gesamte_Sendungen'] > 5].sort_values(by='Verspätungsquote_%', ascending=False)

vendor_performance = get_performance_stats(df, 'Vendor')
site_performance = get_performance_stats(df, 'Manufacturing Site')

print('Top 10 unpünklichste Lieferanten (Vendors):')
print(vendor_performance.head(10))

print('\nTop 10 unpünklichste Produktionsstandorte (Manufacturing Site):')

plt.figure(figsize=(12, 6))
vendor_performance['Verspätungsquote_%'].head(10).plot(kind='bar', color='salmon')

plt.title('Top 10 unpünktlichste Lieferanten (in %)')
plt.ylabel('Verspätung in %')
plt.xlabel('Lieferant (Vendor)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()