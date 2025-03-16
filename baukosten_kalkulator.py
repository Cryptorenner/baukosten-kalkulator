import streamlit as st

def berechne_baukosten(wohnflaeche, kosten_pro_m2, grundstueckskosten, nebenkosten_prozent, sonderausstattung):
    """Berechnet die geschätzten Baukosten für ein Fertighaus."""
    baukosten = wohnflaeche * kosten_pro_m2
    nebenkosten = baukosten * (nebenkosten_prozent / 100)
    gesamtkosten = baukosten + grundstueckskosten + nebenkosten + sonderausstattung
    return baukosten, nebenkosten, gesamtkosten

# Streamlit App Layout
st.set_page_config(page_title="Baukosten-Kalkulator", page_icon="🏡", layout="centered")

st.title("🏡 Baukosten-Kalkulator für Ihr Fertighaus")
st.write("Berechnen Sie in wenigen Sekunden die voraussichtlichen Kosten für Ihr Fertighaus.")

# Eingabefelder
with st.form("baukosten_form"):
    wohnflaeche = st.number_input("Wohnfläche in m²", min_value=50, max_value=500, value=150, step=10)
    kosten_pro_m2 = st.number_input("Durchschnittliche Baukosten pro m² (€)", min_value=1000, max_value=4000, value=2500, step=100)
    grundstueckskosten = st.number_input("Grundstückskosten (€)", min_value=0, max_value=500000, value=100000, step=10000)
    nebenkosten_prozent = st.slider("Nebenkosten (Prozent vom Baupreis)", min_value=5, max_value=30, value=15, step=1)
    sonderausstattung = st.number_input("Kosten für Sonderausstattungen (€)", min_value=0, max_value=100000, value=20000, step=5000)
    
    submit_button = st.form_submit_button("📊 Berechnung starten")

# Berechnung
if submit_button:
    baukosten, nebenkosten, gesamtkosten = berechne_baukosten(wohnflaeche, kosten_pro_m2, grundstueckskosten, nebenkosten_prozent, sonderausstattung)
    
    st.subheader("📊 Ergebnisse Ihrer Berechnung")
    st.write(f"🔹 **Baukosten (ohne Grundstück):** {baukosten:,.2f} €")
    st.write(f"🔹 **Nebenkosten (inkl. Gebühren, Erschließung, etc.):** {nebenkosten:,.2f} €")
    st.write(f"🔹 **Gesamtkosten inkl. Grundstück & Sonderausstattung:** {gesamtkosten:,.2f} €")
    
    st.success("✅ Dies ist eine grobe Schätzung. Lassen Sie uns gemeinsam Ihr Bauvorhaben detailliert planen!")
    st.write("📞 **Kontaktieren Sie uns für eine kostenlose Beratung!**")
