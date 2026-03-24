import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Pro Cocktail Finder", page_icon="🍸", layout="wide")

# Estilo personalizado para colores oscuros
st.markdown("""
    <style>
    .main { background-color: #2c3e50; color: white; }
    .stTextInput search { color: black; }
    </style>
    """, unsafe_allow_html=True)

# Base de datos de recetas
recipes = {
    "LEMON MERINGUE MARTINI": "INGREDIENTS:\n- 30ml Ketel One Citroen\n- 30ml Limoncello\n- 30ml Lemon Juice\n- 5 drops wonderfoam\n\nPREPARATION:\nBuild in shaker, shake and double strain into coupe glass. Garnish with a lemon wheel.",
    "MARGARITA": "INGREDIENTS:\n- 45ml Jose Cuervo Silver\n- 15ml Cointreau\n- 30ml Lime Juice\n- 15ml Simple Syrup\n- (FOR SPICY ADD 5 DROPS TABASCO)\n\nPREPARATION:\nAdd ingredients to shaker, shake and single strain into coupe (or Rocks Gls). Garnish with salted rim (CHILLI SALT for spicy).",
    "LITTLE COLLINS SPRITZ": "INGREDIENTS:\n- 30ml MGC Dry Gin\n- 20ml Blood Orange syrup\n- 15ml lemon juice\n- HALF SODA, HALF ZILZIE SPARKLING\n\nPREPARATION:\nOVER FULL ICE IN A WINE GLASS. TOP HALF SODA, HALF ZILZIE SPARKLING.",
    "MGC SIGNATURE G&T": "INGREDIENTS:\n- 30ml MGC Dry\n- TONIC\n- Ruby grapefruit\n\nPREPARATION:\nBUILD IN A TALL GLASS, ICE, TONIC. rosemary garnish.",
    "HAZELNUT ESPRESSO MARTINI": "INGREDIENTS:\n- 30ml Ketel One Vodka\n- 15ml Kahlua\n- 15ml Frangelico\n- 30ml Fresh espresso\n\nPREPARATION:\nAdd ingredients to shaker, shake and double strain into coupe. Garnish with 3 coffee beans in centre.",
    "TOMMY'S RASPBERRY DELIGHT": "INGREDIENTS:\n- 30ml Pink Gin\n- 30ml Chambord\n- 10ml Grenadine\n- 30ml lime juice\n- 5 drops wonderfoam\n\nPREPARATION:\nBuild in cocktail shaker dry shake, add ice then wet shake, double strain into coupe. Garnish with raspberry sugar on top.",
    "GRANDAD'S FRUITCAKE": "INGREDIENTS:\n- 30ml Wild Turkey American Honey\n- 15ml Dubonnet Rouge\n- 15ml Grand Marnier\n\nPREPARATION:\nBuild in rocks glass over ice. Stir. Garnish with Orange Peel.",
    "NAUGHTY CHOCOLATE ORANGE": "INGREDIENTS:\n- 15ml Cointreau\n- 30ml Brown Creme De Cacao\n- 15ml Baileys\n- Chocolate ice cream\n\nPREPARATION:\nBuild in shaker, Shake and single strain into a coupe over Chocolate ice cream. Garnish with Chocolate powder and orange zest.",
    "APPLE PIE-RATE": "INGREDIENTS:\n- 30ml Sailor Jerry Savage Apple\n- 30ml Captain Morgan Black Spiced\n- 3 dashes orange bitters\n\nPREPARATION:\nBuild in rocks glass over ice. Stir. Garnish with Orange slice.",
    "LIMONCELLO MARGARITA": "INGREDIENTS:\n- 30ml Limoncello\n- 30ml Lime Juice\n- 30ml Jose Cuervo Silver Tequila\n- 15ml Simple Syrup\n\nPREPARATION:\nAdd ingredients to shaker, shake and double strain into coupe. Garnish with Lemon zest.",
    "NECROMANCER": "INGREDIENTS:\n- 30ml Green Fairy Absinthe\n- 30ml Cointreau\n- 15ml Simple Syrup\n- 30ml Lemon Juice\n- 5 drops wonderfoam\n\nPREPARATION:\nBuild in shaker, shake and double strain into coupe. Garnish with Lemon zest.",
    "BAILEYS CHOCOLATE MARTINI": "INGREDIENTS:\n- 30ml Baileys\n- 15ml Ketel One Vodka\n- 15ml Brown Creme de Cacao\n- Chocolate syrup\n\nPREPARATION:\nAdd ingredients to shaker, shake and strain into coupe. Garnish glass with chocolate syrup around the inside of the rim. Top with whipped cream.",
    "ESPRESSO MARTINI": "INGREDIENTS:\n- 45ml Ketel One Vodka\n- 15ml Kaluha\n- 15ml Sugar Syrup\n- 30ml Espresso coffee\n\nPREPARATION:\nShake over ICE. Double strain into COUPE Gls. Garnish with 3 coffee beans.",
    "PASSIONFRUIT DAIQUIRI": "INGREDIENTS:\n- 45ml Bacardi Rum\n- 30ml Lime Juice\n- 30ml Passion Fruit Pulp\n\nPREPARATION:\nShake over ICE. Double Strain into CRYSTAL WINE Gls. Garnish with Lime Wheel.",
    "STRAWBERRY GIN FIZZ": "INGREDIENTS:\n- 45ml Gordons Pink Gin\n- 30ml Lemon Juice\n- 15ml Strawberry Syrup\n- 15ml Sugar Syrup\n- 5 drops Wonderfoam\n\nPREPARATION:\nShake on ICE serve in COUPE glass garnish with strawberry.",
    "COSMOPOLITAN": "INGREDIENTS:\n- 45ml Belvedere Vodka\n- 30ml Cranberry Juice\n- 15ml Cointreau\n- 15ml Lime Juice\n\nPREPARATION:\nShake on ICE, Strain into COUPE Gls. Garnish with Lime Wheel.",
    "MARTINIS": "INGREDIENTS:\n- 60ml Vodka or Gin\n- 10ml Dry Vermouth\n\nPREPARATION:\nMix with ice cubes, Stir well. serve in chilled MARTINI Gls. GARNISH - Squeeze oil from lemon peel onto the drink, or garnish with olive.",
    "CRAN-ROSE SPRITZ": "INGREDIENTS:\n- 60ml Rose wine\n- 60ml Prosecco\n- Cranberry Soda\n\nPREPARATION:\nPour over ICE in WINE Gls. Top with cranberry Soda. Garnish with Orange Wedge.",
    "APEROL SPRITZ": "INGREDIENTS:\n- 60ml Aperol\n- 60ml Prosecco Wine\n- Soda Water\n\nPREPARATION:\nPour over ICE in WINE Gls. Top with Soda. Garnish with Orange Wedge.",
    "JADE SIPPER": "INGREDIENTS:\n- 30ml Midori\n- 30ml Grey Goose\n- 30ml lime juice\n- Yuzu soda\n\nPREPARATION:\nShake and strain into WINE glass. Top with yuzu soda.",
    "LONG ISLAND ICED TEA": "INGREDIENTS:\n- 15ml Bacardi\n- 15ml Skyy Vodka\n- 15ml Gordons Gin\n- 15ml Jose Cuervo Silver\n- 15ml Triple Sec\n- 15ml Lemon Juice\n- Coke\n\nPREPARATION:\nShake and strain into HIGHBALL over ice. Top with Coke.",
    "NEGRONI": "INGREDIENTS:\n- 30ml Gin\n- 30ml Campari\n- 30ml Rosso Antico\n\nPREPARATION:\nStir in mixing glass for 10-15s. Strain into Rocks glass over ice. Garnish with Orange rind.",
}

# Interfaz de usuario
st.title("🍸 Professional Cocktail Finder")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Search")
    search_query = st.text_input("Type cocktail name...", "").upper()
    
    # Filtrar nombres
    names = sorted([n for n in recipes.keys() if search_query in n])
    selected_name = st.radio("Select a cocktail:", names)

with col2:
    st.subheader("Recipe Card")
    if selected_name:
        st.info(f"**{selected_name}**")
        st.code(recipes[selected_name], language="text")
        if st.button("📋 Copy to clipboard"):
            st.write("*(Recipe ready to copy above)*")
