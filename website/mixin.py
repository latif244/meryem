class GermanMixin:
    cinfo = {
        "cName": "A N A S S E",
        "cSlogan": "Hotelservice & Dienstleistungen",
        "cInH": "InH. Anasse Boukari",
        "cAddr": "Koblenzer straße 31",
        "cPLZ": "60327",
        "cCity": "Frankfurt am Main",
        "cState": "Hessen",
        "cTel": "+49 176 638 993 63",
        "cOpnMn": "Mon-DO: 09:00 bis 18:00 Uhr",
        "cOpnFr": "FR: 09:00 bis 15:00 Uhr",
        "message_name": "message_name",
        "cWebsite": "https://anasse.de",
        "cEmail": "info@anasse.de",
        "cQuestions": "Noch Fragen?", #"Have a Questions?",
        "cOpenHrs": "Geschäftszeiten",
        "cOpenDays": "Öffnungstage:",
        "cEmergency": "Für Notfälle",
        "cVaccation": "Ferien",
        "cWorks": "Die Art von Arbeiten, die wir ausführen",
        "cSubheading": "Sauber Räume, glückliche Gesichter",
        "cFriendly": "Wir verwenden umweltfreundliche Reinigungsprodukte für Kunden, die ökologische Reinigungslösungen bevorzugen.",
        "cMission": "Unsere Mission ist es, das vertrauenswürdigste und zuverlässigste Reinigungsunternehmen in der Region zu werden. Wir werden dies erreichen, indem wir außergewöhnliche Reinigungsdienste anbieten, umweltfreundliche Reinigungsprodukte verwenden und wettbewerbsfähige Preise anbieten.",
        "cQLinks":"Quick Links",
        "cNHome":"Willkommen",
        "cNAbout":"Über uns",
        "cNServices":"Dienstleistung",
        "cNBlog":"Stellenangebote",
        "cNContact":"Kontakt",
        "cSOffice":"GEBÄUDEREINIGUNG",
        "cSOfficeSl":"Wir stellen Ihnen kompetente Mitarbeiter zur Verfügung. Sei es für Grundreinigungen oder den täglichen Bedarf.Unterhaltsreinigung, Büroreinigung, Wellness- und Spa- Bereiche,Glasreinigung, Teppichreinigung / Shampoonierarbeiten",
        "cSKitchen":"STEWARDING",
        "cSKitchenSl":"Die Küche bedarf der ständigen Beobachtung hinsichtlich Qualität und Kosten. Die Entlastung in der Personal disposition ermöglicht Ihnen die Konzentration auf IHR Kerngeschäft. Wir sind in diesem Bereich Ihr Ansprechpartner und zeichnen uns aus durch langjährige Erfahrung und Kompetenz.",
        "cSRezeption":"Rezeption",
        "cSRezeptionSl":"Ein freundlicher und kompetenter Empfang ist der Schlüssel eines gastfreundlichen Hauses, hier bieten Wir Ihnen passendes Personal um Ihren Standard zu gewährleisten. Sprechen Sie uns an.",
        "cSService":"Service",
        "cSServiceSl":"Dienstleistung ist unsere Leidenschaft! Sei es im Restaurantservice, Bankett oder Gala wir bieten Ihnen die passenden kooperations- Möglichkeiten",
        "cSHousekeep":"Housekeeping",
        "cSHousekeepSl":"Two smiling cleaners cleaning room together Anasse Hotelservice steht für Reinigungsarbeiten der extra klasse! Zimmereinigung Bereitstellung von Hausdamen Minibar service Abdeckservice/ Turndown Betten und Wäschedienste Matratzenreinigung Pflege von Public Areas und Außenanlagen Konferenzservice Vorarbeiter zur Einarbeitung Allgemeiner ersonalservice Im allgemeinen bieten wir Ihnen folgende Dienstleistungen, hier unsere Leistungen im Überblick:",
        "cSCatering":"Catering",
        "cSCateringSl":"Bankett- und Konferenzservice Personaldienste Empfangsservice Post- und Botendienste Schmutzfangmattenservice Hausmeisterservice",
    }
    
    my_data1 = {
        'product': 'Laptop',
        'brand': 'Lenovo',
        'model': 'Thinkpad Carbon X1'
    }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinfo'] = self.cinfo
        context['my_data1'] = self.my_data1
        return context