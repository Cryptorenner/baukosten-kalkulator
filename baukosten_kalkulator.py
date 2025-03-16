import streamlit as st

def berechne_baukosten(wohnflaeche, kosten_pro_m2, grundstueckspreis, grundstueckskosten, nebenkosten_prozent, sonderausstattung):
    """Berechnet die geschätzten Baukosten für ein Fertighaus."""
    baukosten = wohnflaeche * kosten_pro_m2
    nebenkosten = baukosten * (nebenkosten_prozent / 100)
    gesamtkosten = baukosten + grundstueckspreis + grundstueckskosten + nebenkosten + sonderausstattung
    return baukosten, nebenkosten, gesamtkosten

def berechne_monatliche_rate(kreditsumme, zinssatz, laufzeit):
    """Berechnet die monatliche Darlehensrate."""
    zinssatz_monatlich = zinssatz / 100 / 12
    anzahl_monate = laufzeit * 12
    if zinssatz_monatlich > 0:
        rate = (kreditsumme * zinssatz_monatlich) / (1 - (1 + zinssatz_monatlich) ** -anzahl_monate)
    else:
        rate = kreditsumme / anzahl_monate
    return rate

# Streamlit App Layout
st.set_page_config(page_title="Baukosten- & Finanzierungskalkulator", page_icon="🏡", layout="centered")

st.title("🏡 Baukosten- & Finanzierungskalkulator für Ihr Fertighaus")
st.write("Berechnen Sie die voraussichtlichen Kosten Ihres Bauprojekts und die monatliche Finanzierungsrate.")

# Eingabefelder für Baukosten
with st.form("baukosten_form"):
    wohnflaeche = st.number_input("Wohnfläche in m²", min_value=50, max_value=500, value=150, step=10)
    kosten_pro_m2 = st.number_input("Durchschnittliche Baukosten pro m² (€)", min_value=1000, max_value=4000, value=2500, step=100)
    grundstueckspreis = st.number_input("Grundstückspreis pro m² (€)", min_value=0, max_value=2000, value=500, step=50)
    grundstuecksgroesse = st.number_input("Grundstücksgröße in m²", min_value=100, max_value=5000, value=500, step=50)
    grundstueckskosten = grundstueckspreis * grundstuecksgroesse
    nebenkosten_prozent = st.slider("Nebenkosten (Prozent vom Baupreis)", min_value=5, max_value=30, value=15, step=1)
    sonderausstattung = st.number_input("Kosten für Sonderausstattungen (€)", min_value=0, max_value=100000, value=20000, step=5000)
    
    submit_button = st.form_submit_button("📊 Berechnung starten")

# Berechnung der Baukosten
if submit_button:
    baukosten, nebenkosten, gesamtkosten = berechne_baukosten(wohnflaeche, kosten_pro_m2, grundstueckspreis, grundstueckskosten, nebenkosten_prozent, sonderausstattung)
    
    st.subheader("📊 Ergebnisse Ihrer Baukostenberechnung")
    st.write(f"🔹 **Baukosten (ohne Grundstück):** {baukosten:,.2f} €")
    st.write(f"🔹 **Grundstückskosten:** {grundstueckskosten:,.2f} €")
    st.write(f"🔹 **Nebenkosten (inkl. Gebühren, Erschließung, etc.):** {nebenkosten:,.2f} €")
    st.write(f"🔹 **Gesamtkosten inkl. Grundstück & Sonderausstattung:** {gesamtkosten:,.2f} €")
    
    st.success("✅ Dies ist eine grobe Schätzung. Lassen Sie uns gemeinsam Ihr Bauvorhaben detailliert planen!")
    st.write("📞 **Kontaktieren Sie uns für eine kostenlose Beratung!**")

# Finanzierungskalkulator
st.header("💰 Finanzierungskalkulator")
st.write("Berechnen Sie die voraussichtliche monatliche Rate für Ihre Baufinanzierung.")

# Hinweis auf aktuelle Zinssätze
st.info("💡 Aktuelle Zinssätze für Baufinanzierungen liegen je nach Bank zwischen **3,5% - 5,5% p.a.** (Stand 2025).")

# Eingaben für Finanzierungsrechner
kreditsumme = st.number_input("Benötigte Kreditsumme (€)", min_value=10000, max_value=5000000, value=int(gesamtkosten), step=10000)
zinssatz = st.slider("Zinssatz (% p.a.)", min_value=1.0, max_value=10.0, value=4.0, step=0.1)
laufzeit = st.slider("Laufzeit des Kredits (Jahre)", min_value=5, max_value=35, value=20, step=1)

# Berechnung der monatlichen Rate
monatliche_rate = berechne_monatliche_rate(kreditsumme, zinssatz, laufzeit)

st.subheader("📊 Ergebnisse der Finanzierungsberechnung")
st.write(f"💰 **Monatliche Rate:** {monatliche_rate:,.2f} €")
st.write(f"📅 **Gesamtkosten des Kredits über {laufzeit} Jahre:** {monatliche_rate * laufzeit * 12:,.2f} €")

st.success("✅ Planen Sie Ihre Finanzierung mit diesen Werten und kontaktieren Sie uns für weitere Beratung!")


