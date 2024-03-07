import requests                           # For sending HTTP requests and fetching data from websites.
import pandas as pd                       # For data manipulation and analysis with DataFrame structures.
import re                                 # For working with regular expressions for pattern matching and text processing.
from IPython.display import display, HTML # For displaying rich content in IPython environments.
import seaborn as sns                     # For creating attractive and informative statistical graphics.
import matplotlib.pyplot as plt           # For creating plots and visualizations.
import matplotlib.colors as mcolors       # For working with colors in Matplotlib plots.
import numpy as np                        # For numerical computations and data manipulation with arrays.


def extract_value(cell):
    return cell[1]


def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())


def extract_year(appearance):
    year_pattern = r'\b\d{4}\b'
    match = re.search(year_pattern, appearance)
    
    if match:
        return match.group()
    else:
        return None


def render_image(url):
    return f'<img src="{url}" style="max-width:75px; height:auto;">'

    def get_top_10(df, column_name):
    top_10 = df.nlargest(10, column_name)
    
    image_column = top_10.pop('Image')
    top_10.insert(1, 'Image', image_column) 

    def render_image(url):
        return f'<img src="{url}" style="max-width:75px; height:auto;">'

    top_10['Image'] = top_10['Image'].apply(render_image)

    html = top_10.to_html(escape=False)


def get_top_10(df, column_name):
    top_10 = df.nlargest(10, column_name)
    
    image_column = top_10.pop('Image')
    top_10.insert(1, 'Image', image_column) 


    def render_image(url):
        return f'<img src="{url}" style="max-width:75px; height:auto;">'

    top_10['Image'] = top_10['Image'].apply(render_image)

    html = top_10.to_html(escape=False)

    display(HTML(html))


def get_top_10_with_condition(df, column_name, condition_column, condition_values):
    filtered_df = df[df[condition_column].isin(condition_values)]
    
    top_10 = filtered_df.nlargest(10, column_name)
    
    image_column = top_10.pop('Image')
    top_10.insert(1, 'Image', image_column) 


    def render_image(url):
        return f'<img src="{url}" style="max-width:75px; height:auto;">'

    top_10['Image'] = top_10['Image'].apply(render_image)

    html = top_10.to_html(escape=False)

    display(HTML(html))



def plot_top_values(df, column_name, top_n=10, palette='husl'):
   
    top_values = df[column_name].value_counts().nlargest(top_n).index
    
    df_top_values = df[df[column_name].isin(top_values)]
    
    unique_values = len(top_values)
    custom_palette = sns.color_palette(palette, unique_values)
    
    sns.countplot(y=column_name, data=df_top_values, hue=column_name, order=top_values, palette=custom_palette, legend=False)
    plt.title(f'Count {column_name}s')
    plt.ylabel(column_name)
    plt.xlabel('Count')
    plt.xticks(rotation=45, ha='right')
    
    for p in plt.gca().patches:
        plt.gca().annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2.),
                           ha='center', va='center', fontsize=8, color='black', xytext=(8, 0),
                           textcoords='offset points')
    
    plt.tight_layout()
    plt.show()


def generate_pie_chart(df, column_name, colors=None):
    value_counts = df[column_name].value_counts()
    
    labels = value_counts.index
    counts = value_counts.values
    
    if colors is None:
        colors = plt.cm.tab20.colors[:len(labels)]
    
    plt.figure(figsize=(8, 6))
    wedges, texts, autotexts = plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    
    for i, label in enumerate(labels):
        texts[i].set_text(f'{label} ({counts[i]})')

    plt.title(f'Distribution of {column_name} values')
    plt.axis('equal') 
    plt.show()


def compare_evil_vs_good(df):
    evil_df = df[df['Alignment'] == '😈']
    good_df = df[df['Alignment'] == '😇']
    
    evil_count = len(evil_df)
    good_count = len(good_df)
    evil_sum = evil_df['Overall PS'].sum()
    good_sum = good_df['Overall PS'].sum()

    categories = ['😈', '😇']
    counts = [evil_count, good_count]
    sums = [evil_sum, good_sum]

    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Alignment')
    ax1.set_ylabel('Counts', color=color)
    ax1.bar(categories, counts, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  
    color = 'tab:red'
    ax2.set_ylabel('Overall PS Sum', color=color)
    ax2.plot(categories, sums, color=color, marker='o', linestyle='--')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  
    plt.title('Comparison between Evil and Good')
    plt.show()


def compare_avg_evil_vs_good(df):
    evil_df = df[df['Alignment'] == '😈']
    good_df = df[df['Alignment'] == '😇']
    
    avg_evil_overall_ps = evil_df['Overall PS'].mean()
    avg_good_overall_ps = good_df['Overall PS'].mean()
    
    categories = ['😈', '😇']
    averages = [avg_evil_overall_ps, avg_good_overall_ps]

    plt.bar(categories, averages, color=['firebrick', 'green'])
    plt.title('Average Overall PS: Evil vs Good')
    plt.xlabel('Alignment')
    plt.ylabel('Average Overall PS')
    
    for i, value in enumerate(averages):
        plt.text(i, value + 0.05, f'{value:.2f}', ha='center')
    
    plt.show()


def compare_avg_top_10_evil_vs_good(df):
    top_10_evil = df[df['Alignment'] == '😈'].nlargest(10, 'Overall PS')
    top_10_good = df[df['Alignment'] == '😇'].nlargest(10, 'Overall PS')
    
    avg_top_10_evil_overall_ps = top_10_evil['Overall PS'].mean()
    avg_top_10_good_overall_ps = top_10_good['Overall PS'].mean()
    
    categories = ['😈', '😇']
    averages = [avg_top_10_evil_overall_ps, avg_top_10_good_overall_ps]

    plt.bar(categories, averages, color=['firebrick', 'green'])
    plt.title('Average Overall PS: Top 10 Evil vs Top 10 Good')
    plt.xlabel('Alignment')
    plt.ylabel('Average Overall PS')

    for i, value in enumerate(averages):
        plt.text(i, value + 0.05, f'{value:.2f}', ha='center')

    plt.show()


def filter_heroes(df):
    print("Welcome to the hero selection tool!")
    print("Please define your filters for hero selection:")

    race = input("Enter the race of heroes (e.g., Human, Alien, etc.): ")
    alignment = input("Enter the alignment of heroes (e.g., 😇 for good, 😈 for evil): ")

    filtered_df = df[(df['Race'] == race) & (df['Alignment'] == alignment)]
    
    return filtered_df

def display_heroes(df):
    print("\nList of Heroes:")
    print(df[['Name', 'Overall PS', 'PS Intelligence', 'PS Strength', 'PS Speed', 'PS Durability', 'PS Power', 'PS Combat']])

def select_team(df):
    team = []
    total_overall_ps = 0
    
    while len(team) < 5:
        hero_name = input(f"\nChoose hero {len(team) + 1}: ")
        hero = df[df['Name'] == hero_name]
        
        if len(hero) == 0:
            print("Hero not found. Please choose from the list.")
        else:
            hero_overall_ps = hero['Overall PS'].values[0]
            if total_overall_ps + hero_overall_ps > 15000:
                print("Total overall PS exceeds 15000. Cannot add more heroes to the team.")
                break
            else:
                team.append(hero)
                total_overall_ps += hero_overall_ps
                print(f"{hero_name} added to the team.")
    
    return team

def main():
    try:
        filtered_df = filter_heroes(df_cleaned_formatted)
        
        display_heroes(filtered_df)
        
        team = select_team(filtered_df)
        
        print("\nSelected Team:")
        for hero in team:
            print(hero['Name'].values[0])
    
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
