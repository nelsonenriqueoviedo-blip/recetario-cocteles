import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cocktail Finder Pro", page_icon="🍸", layout="centered")

# Estilo CSS para salto de línea automático y diseño limpio
st.markdown("""
    <style>
    .main { background-color: #2c3e50; }
    .recipe-box {
        background-color: #ecf0f1;
        color: #2c3e50;
        padding: 25px;
        border-radius: 10px;
        font-family: 'Consolas', monospace;
        font-size: 1.1rem;
        line-height: 1.6;
        white-space: pre-wrap;
        word-wrap: break-word;
        border-left: 5px solid #27ae60;
    }
    div.stButton > button { width: 100%; background-color: #27ae60; color: white; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Base de datos completa
recipes = {
    # --- SANGRÍAS (VERSIONES CARAFE Y SINGLE) ---
    "PINEAPPLE LEMONADE SANGRIA (CARAFE)": "INGREDIENTS:\n- 375ml Jade Estate White\n- 60ml Triple Sec\n- 250ml Lemonade\n- 250ml Pineapple Juice\n\nPREPARATION:\nBuild in carafe, stir, add ice. Garnish with pineapple and orange.",
    
    "PINEAPPLE LEMONADE SANGRIA (SINGLE)": "INGREDIENTS:\n- 90ml Jade Estate White\n- 15ml Brandy (or Triple Sec per Carafe recipe)\n- 60ml Lemonade\n- 60ml Pineapple Juice\n\nPREPARATION:\nBuild in glass over ice. Stir well. Garnish with pineapple and orange.",
    
    "STRAWBERRY SANGRIA (CARAFE)": "INGREDIENTS:\n- 375ml Jade Estate Red\n- 60ml Brandy\n- 250ml Lemonade\n- 250ml Apple Juice\n\nPREPARATION:\nBuild in carafe, stir, add ice. Garnish with strawberry and orange.",
    
    "SINGLE SERVE STRAWBERRY SANGRIA": "INGREDIENTS:\n- 90ml Jade Estate Red\n- 15ml Brandy\n- 60ml Lemonade\n- 60ml Apple Juice\n\nPREPARATION:\nBuild in glass over ice. Stir well. Garnish with fruit.",

    # --- OTROS DE LA IMAGEN ---
    "PINA COLADA": "INGREDIENTS:\n- 60ml Malibu\n- 60ml Coconut Cream\n- 120ml Pineapple Juice\n\nPREPARATION:\nShake in tin with crushed ice. Serve in Hurricane glass. Garnish with pineapple wedge and leaf.",
    
    "MARGY MOCKTAIL": "INGREDIENTS:\n- 45ml Lime Juice\n- 15ml Lemon Juice\n- 15ml Orange Juice\n- 15-25ml Simple Syrup\n\nPREPARATION:\nSalt rim glass. Build in shaker. Add ice + shake + strain. Serve in coupe or rocks glass. Add Sprite for dilution if needed.",
    
    "TROPICAL MOCKTAIL": "INGREDIENTS:\n- 60ml Pineapple Juice\n- 30ml Orange Juice\n- 30ml Lime Juice\n- 15-30ml Passionfruit\n- 15ml Simple Syrup\n\nPREPARATION:\nBuild in shaker. Add ice + shake + single strain. Serve in hurricane or Chablis glass. Top with Lemonade/Sprite.",
    
    "PASSION MOCKTAIL": "INGREDIENTS:\n- 45ml Passionfruit Pulp\n- 30ml Lime Juice\n- 15ml Orange Juice\n- 15ml Simple Syrup\n\nPREPARATION:\nBuild in shaker. Add ice + shake + strain. Serve in coupe or rocks glass. Top with lemonade if needed.",

    # --- COCTELES CLÁSICOS Y ESPECIALES ---
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
    "NEGRONI": "INGREDIENTS:\n- 30ml Hendricks or Bombay or Sloe Gin\n- 30ml Campari\n- 30ml Rosso Antico - Sweet Vermouth\n\nPREPARATION:\nStir in mixing glass for 10-15s. Strain into Rocks glass over ice. Garnish with Orange rind.",
    "OLD FASHIONED": "INGREDIENTS:\n- 60ml Woodford Reserve\n- 5 dashes Angostura\n- 10ml Sugar Syrup\n\nPREPARATION:\nBuild in mixing glass, stir over ice. Strain into rocks glass. Orange peel garnish.",
    "AMARETTO SOUR": "INGREDIENTS:\n- 45ml Amaretto\n- 15ml Makers Mark\n- 30ml Lemon Juice\n- 5ml Sugar Syrup\n- 5 drops Wonderfoam\n\nPREPARATION:\nShake and double strain into Rocks glass.",
    "MEXICAN MULE": "INGREDIENTS:\n- 45ml 1800 Silver\n- 30ml Lime Juice\n- Ginger Beer\n\nPREPARATION:\nBuild in highball glass. Top with Ginger Beer. Garnish with lime and mint.",
    "WHISKEY SMASH": "INGREDIENTS:\n- 60ml Dickle Whiskey\n- 15ml Sugar Syrup\n- 15ml St Germaine\n- 5 slices lemon\n\nPREPARATION:\nMuddle lemon/mint. Shake and double strain into Rocks glass.",
    "PINK PINK PONNEY": "INGREDIENTS:\n- 30ml GORDONS PINK GIN\n- 30ml Sloe GIN\n- 15ml Lime Juice\n\nPREPARATION:\nStir in mixing glass for 10-15s. Strain into Rocks glass (Garnish with Pink suggar rim) over ice, top with soda.",
    "JALEPINO PINEAPPLE MARGARITA": "INGREDIENTS:\n- 30ml Jose Cuervo Silver\n- 15ml Cointreau\n- 60ml Lime Juice\n- 15ml Simple Syrup\n\nPREPARATION:\nMuddle 3 Jalapeno. Shake on ICE. Strain into ROCKS Gls."
}

st.title("🍸 Cocktail Finder")

# Buscador
search_query = st.text_input("Search Cocktail:", key="search_bar").upper()

if search_query:
    # Filtrado inteligente
    options = sorted([name for name in recipes.keys() if search_query in name])
    
    if options:
        selected_cocktail = st.selectbox("Suggestions Found:", options)
        
        if selected_cocktail:
            st.markdown(f"### {selected_cocktail}")
            st.markdown(f'<div class="recipe-box">{recipes[selected_cocktail]}</div>', unsafe_allow_html=True)
            
            if st.button("Copy Recipe"):
                st.success("You can now select the text above and copy it easily!")
    else:
        st.warning("No cocktail found with that name.")
else:
    st.info("Start typing to find a recipe. Try 'Sangria' or 'Mocktail'!")
