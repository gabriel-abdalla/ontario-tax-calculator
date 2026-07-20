import streamlit as st

st.title("Ontario Take-Home Pay Calculator")

income = st.number_input("What is your income per year?", min_value=0, step=1000)

income = int(income)

if income > 0:

    takehome_pay = 0
    provincial = 12989
    federal = 16452
    pension_plan = 3500


    # Employment Insurance
    if income < 68900:
        employment_insurance = income * (1.63 / 100)
    else:
        employment_insurance = 1123.07


    # CPP
    if income <= 74600:
        pension_tax = (income - pension_plan) * (5.95 / 100)
    elif income >= 85000:
        pension_tax = 4646.45
    else:
        pension_tax = 4230.45 + ((income - 74600) * (4 / 100))


    # Federal Taxes
    if income <= federal:
        federal_tax = 0
    elif income <= 58523:
        federal_tax = (income - federal) * 0.14
    elif income <= 117045:
        federal_tax = ((income - 58523) * 0.205) + (42071 * 0.14)
    elif income <= 181440:
        federal_tax = ((income - 117045) * 0.26) + ((117045 - 58523) * 0.205) + (42071 * 0.14)
    elif income <= 258482:
        federal_tax = ((income - 181440) * 0.29) + ((181440 - 117045) * 0.26) + ((117045 - 58523) * 0.205) + (42071 * 0.14)
    else:
        federal_tax = ((income - 258482) * 0.33) + ((258482 - 181440) * 0.29) + ((181440 - 117045) * 0.26) + ((117045 - 58523) * 0.205) + (42071 * 0.14)


    if income > federal:
        federal_tax = federal_tax - ((1400 + pension_tax + employment_insurance) * 0.14)



    # Provincial Taxes
    if income <= provincial:
        provincial_tax = 0
    elif income <= 53891:
        provincial_tax = (income - provincial) * 0.0505
    elif income <= 107785:
        provincial_tax = ((income - 53891) * 0.0915) + (40902 * 0.0505)
    elif income <= 150000:
        provincial_tax = ((income - 107785) * 0.1116) + ((107785 - 53891) * 0.0915) + (40902 * 0.0505)
    elif income <= 220000:
        provincial_tax = ((income - 150000) * 0.1216) + ((150000 - 107785) * 0.1116) + ((107785 - 53891) * 0.0915) + (40902 * 0.0505)
    else:
        provincial_tax = ((income - 220000) * 0.1316) + ((220000 - 150000) * 0.1216) + ((150000 - 107785) * 0.1116) + ((107785 - 53891) * 0.0915) + (40902 * 0.0505)


    # Ontario surtax
    if provincial_tax <= 5818:
        surtax = 0
    elif provincial_tax <= 7446:
        surtax = 0.2 * (provincial_tax - 5818)
    else:
        surtax = (0.2 * (provincial_tax - 5818)) + (0.36 * (provincial_tax - 7446))


    if income > provincial:
        provincial_tax += surtax
        provincial_tax -= (pension_tax + employment_insurance) * 0.0505



    # Ontario Health Premium
    taxable_income = income - pension_tax - employment_insurance

    if taxable_income <= 20000:
        ontario_health_care_tax = 0
    elif taxable_income <= 36000:
        ontario_health_care_tax = min((taxable_income - 20000) * 0.06, 300)
    elif taxable_income <= 48000:
        ontario_health_care_tax = min(((taxable_income - 36000) * 0.06) + 300, 450)
    elif taxable_income <= 72000:
        ontario_health_care_tax = min(((taxable_income - 48000) * 0.25) + 450, 600)
    elif taxable_income <= 200000:
        ontario_health_care_tax = 600
    elif taxable_income <= 200600:
        ontario_health_care_tax = min(((taxable_income - 200000) * 0.25) + 600, 900)
    else:
        ontario_health_care_tax = 900


    takehome_pay = income - (
        federal_tax +
        provincial_tax +
        employment_insurance +
        pension_tax +
        ontario_health_care_tax
    )


    st.subheader("Tax Breakdown")

    st.write(f"Federal Tax: ${federal_tax:,.2f}")
    st.write(f"Provincial Tax: ${provincial_tax:,.2f}")
    st.write(f"Employment Insurance: ${employment_insurance:,.2f}")
    st.write(f"CPP: ${pension_tax:,.2f}")
    st.write(f"Ontario Health Premium: ${ontario_health_care_tax:,.2f}")

    st.success(f"Take-home Pay: ${takehome_pay:,.2f}")