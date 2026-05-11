<template>
  <div id="app">
    <Header />
    <main class="main-content">
      <!-- Progress banner -->
      <div id="top" class="progress-banner">
        <div class="progress-content">
          <div class="progress-text">
            <h3>Jouw 18e jaar checklist</h3>
            <p>Je bent <strong>{{ overallProgress }}% voorbereid</strong> blijf zo doorgaan!</p>
          </div>
          <div class="journey-meta">
            <div class="journey-pill">XP: {{ journeyPoints }}</div>
            <div class="journey-pill">Badges: {{ completedCount }}/{{ features.length }}</div>
            <div class="journey-pill">Volgende stap: {{ nextIncompleteTitle }}</div>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: overallProgress + '%' }"></div>
          </div>
          <div class="progress-items">
            <div v-for="(feat, idx) in features" :key="idx" class="progress-item" :class="{ done: feat.completed }">
              <span class="icon">{{ feat.completed ? '✓' : idx+1 }}</span>
              <span class="label">{{ feat.titleShort }}</span>
            </div>
          </div>
        </div>
      </div>

      <section class="hero">
        <div class="hero-content">
          <h1 class="hero-title">Van 17 naar 18<br><span>Alles geregeld?</span></h1>
          <p class="hero-subtitle">Studiefinanciering, OV, zorgtoeslag, huurtoeslag, WatNu18 geeft je stap voor stap duidelijkheid. Gemaakt door MBO'ers, voor MBO'ers.</p>
          <button class="cta-btn" @click="scrollToFeatures">Start je journey →</button>
        </div>
      </section>

    <section class="lower-half" id="half">
      <section class="features" id="features">
        <div class="features-wrapper">
          <div class="section-header">
            <h2>Jouw 7‑stappen plan</h2>
            <p>Voltooi elke stap, verdien badges en word volledig voorbereid voor je 18e en daarna</p>
          </div>
          <div class="feature-rail-controls" aria-hidden="true">
            <button class="rail-btn" @click="scrollFeatureRail(-1)">←</button>
            <button class="rail-btn" @click="scrollFeatureRail(1)">→</button>
          </div>
          <div class="features-grid" ref="featureRail">
            <div class="feature-card" v-for="(feature, index) in features" :key="index" :id="feature.anchor" :class="{ completed: feature.completed }">
              <div class="feature-header">
                <span class="feature-step">{{ index + 1 }}</span>
                <span class="feature-badge" v-if="feature.completed">✓ Voltooid</span>
              </div>
              <h3>{{ feature.title }}</h3>
              <p>{{ feature.description }}</p>
              <ul class="feature-highlights">
                <li v-for="(tip, tipIndex) in feature.quickTips" :key="`${index}-${tipIndex}`">{{ tip }}</li>
              </ul>
              <button class="feature-btn" @click="selectFeature(index)">
                {{ feature.completed ? 'Herbekijk' : 'Start missie' }}
              </button>
            </div>
          </div>
        </div>
      </section>
    </section>

      <section class="details" v-if="selectedFeature !== null" @click.self="selectedFeature = null">
        <div class="details-container">
          <button class="close-btn" @click="selectedFeature = null">← Terug naar overzicht</button>
          <div class="details-content">
            <h2>{{ features[selectedFeature].title }}</h2>
            <p>{{ features[selectedFeature].longDescription }}</p>
            <div class="detail-faq">
              <button class="faq-toggle-btn" @click="expandedFaqs = !expandedFaqs">
                <h3>Veelgestelde vragen over deze stap</h3>
                <span class="toggle-arrow" :class="{ expanded: expandedFaqs }">▼</span>
              </button>
              <div class="faq-list" v-if="expandedFaqs">
                <div class="faq-item" v-for="(faq, faqIndex) in features[selectedFeature].faqs" :key="faqIndex">
                  <h4>{{ faq.question }}</h4>
                  <p>{{ faq.answer }}</p>
                </div>
              </div>
            </div>
            <div class="details-quiz" v-if="features[selectedFeature].quiz">
              <h3>Check je kennis</h3>
              <div class="quiz-question">
                <p>{{ features[selectedFeature].quiz.question }}</p>
                <div class="quiz-options" v-if="!quizAttempted || !quizResult.isCorrect">
                  <button class="quiz-option" v-for="(option, i) in features[selectedFeature].quiz.options" :key="i"
                    @click="submitQuizAnswer(i)" :class="{ selected: currentQuizAnswer === i }"
                    :disabled="quizAttempted && !quizResult.isCorrect">
                    {{ option }}
                  </button>
                </div>
                <div class="quiz-result" v-if="quizAttempted && quizResult">
                  <div class="quiz-feedback" :class="quizResult.isCorrect ? 'correct' : 'incorrect'">
                    <div class="feedback-icon">{{ quizResult.isCorrect ? '' : '' }}</div>
                    <div class="feedback-text">
                      <h4>{{ quizResult.isCorrect ? 'Goed gedaan!' : 'Niet helemaal' }}</h4>
                      <p>{{ quizResult.explanation }}</p>
                    </div>
                  </div>
                  <button v-if="quizResult.isCorrect" class="quiz-action-btn completed" disabled>
                    Badge verdiend
                  </button>
                  <button v-else class="quiz-action-btn retry" @click="retryQuiz">
                    Opnieuw proberen
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Why WatNu18 -->
      <section class="info-section">
        <h2>Waarom WatNu18?</h2>
        <div class="info-grid">
          <div class="info-card">
            <div class="info-icon">🎯</div>
            <h3>Speciaal voor MBO</h3>
            <p>Geen overbodige info — alleen wat jij écht nodig hebt. Ook info over doorstroom naar HBO, schuld en wat gebeurt als je stopt.</p>
          </div>
          <div class="info-card">
            <div class="info-icon">📋</div>
            <h3>Gebaseerd op DUO & overheid</h3>
            <p>Alle informatie up‑to‑date en betrouwbaar, getoetst door experts. Bedragen en deadlines worden continu gecontroleerd.</p>
          </div>
          <div class="info-card">
            <div class="info-icon">🏆</div>
            <h3>Motiverend & gamified</h3>
            <p>Verdien badges, volg je voortgang en stap-voor-stap naar 100%! Je gaat beter voorbereid de wereld in.</p>
          </div>
          <div class="info-card">
            <div class="info-icon">💬</div>
            <h3>Chatbot Noa helpt 24/7</h3>
            <p>Stel je vragen in Nederlands. Noa antwoordt praktisch en eerlijk — ook over moeilijke onderwerpen als schuld.</p>
          </div>
          <div class="info-card">
            <div class="info-icon">📱</div>
            <h3>Gratis & geen account</h3>
            <p>Geen login nodig, geen kosten, geen reclame. Gewoon kennis recht in je browser. Door MBO'ers, voor MBO'ers.</p>
          </div>
          <div class="info-card">
            <div class="info-icon">✨</div>
            <h3>Echte student stories</h3>
            <p>Lees hoe anderen hun 18e voorbereidden. Van eerstejaars tot alumni: hun tips en tips helpen jou.</p>
          </div>
        </div>
      </section>
      
      <!-- Student Stories -->
      <section class="stories-section" id="stories">
        <div class="stories-inner">
          <h2>Echte verhalen van MBO'ers</h2>
          <p>Inspiratie en tips van jongeren die net als jij 18 werden en hun zaakjes regelden.</p>
          <div class="stories-grid">
            <article class="story-card">
              <div class="story-avatar">👩‍🎓</div>
              <h3>Lisa (MBO Verpleegkunde)</h3>
              <p class="story-role">Jaar 2 → Doorstroom HBO</p>
              <p class="story-text">"Ik was bang dat doorstroom naar HBO ingewikkeld was. Maar DUO regelde alles automatisch! Ik kreeg bijna hetzelfde geld. Tips: meld je HBO-inschrijving op tijd en check je Mijn DUO twee weken voor start."</p>
              <div class="story-tip">💡 Tip: Doorstroom is makkelijker dan je denkt!</div>
            </article>
            <article class="story-card">
              <div class="story-avatar">👨‍🔧</div>
              <h3>Ruben (MBO Elektrotechniek)</h3>
              <p class="story-role">Bijbaan + Studiefinanciering</p>
              <p class="story-text">"Ik verdiende €400/maand in een bijbaan. Ik vertelde DUO NIET en toen verloor ik mijn extra beurs. Advies: meld alles wat je verdient. Beter 1x onhandig dan straks terugbetalen!"</p>
              <div class="story-tip">💡 Tip: Meld je bijbaan ALTIJD aan DUO!</div>
            </article>
            <article class="story-card">
              <div class="story-avatar">👩‍💼</div>
              <h3>Amira (MBO Administratie)</h3>
              <p class="story-role">Op kamers gaan</p>
              <p class="story-text">"Huurtoeslag was mijn reddingslijn. Zonder zou ik €250/maand niet betaald hebben. Tricky: ik moest eerst zeggen dat mijn keuken zelfstandig was. Niet gelogen, maar wel duidelijk communiceren!"</p>
              <div class="story-tip">💡 Tip: Huurtoeslag vraag je VROEG aan!</div>
            </article>
            <article class="story-card">
              <div class="story-avatar">👨‍🎓</div>
              <h3>Sam (MBO → HBO → Werk)</h3>
              <p class="story-role">School → Werk → Schuld</p>
              <p class="story-text">"Ik heb 4 jaar MBO + 4 jaar HBO gedaan. Schuld was ca. €24.000. Maar als je gaat werken verdien je genoeg om af te betalen. Nu betaal ik ca. €150/maand. Doable!"</p>
              <div class="story-tip">💡 Tip: Schuld is niet het einde van de wereld!</div>
            </article>
          </div>
        </div>
      </section>
      <section class="faq-section" id="faq">
        <div class="faq-section-inner">
          <h2>Extra veelgestelde vragen</h2>
          <p>Snelle antwoorden op vragen die je als eerstejaars vaak meteen wilt weten.</p>
          <div class="faq-overview-grid">
            <article class="faq-overview-card" v-for="(item, idx) in extraFaqs" :key="idx">
              <h3>{{ item.question }}</h3>
              <p>{{ item.answer }}</p>
            </article>
          </div>
        </div>
      </section>
    </main>
    <LegalSections />
    <Footer />
    <ChatWidget />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import LegalSections from './components/LegalSections.vue'
import ChatWidget from './components/ChatWidget.vue'
import { ref, computed, watch, nextTick, onMounted, provide } from 'vue'
import { siteNavigationKey } from './composables/siteNavigation.js'

const selectedFeature = ref(null)
const currentQuizAnswer = ref(null)
const quizResult = ref(null)
const quizAttempted = ref(false)
const featureRail = ref(null)
const expandedFaqs = ref(false)
const PROGRESS_STORAGE_KEY = 'watnu18_feature_progress_v1'

const features = ref([
  {
    title: 'Studiefinanciering',
    anchor: 'studiefinanciering',
    titleShort: 'DUO',
    description: 'Begrijp hoe DUO werkt en wat je kunt aanvragen.',
    longDescription: `Studiefinanciering van DUO is financiële ondersteuning voor studenten. Je kunt aanvragen zodra je 18 bent en een erkende opleiding volgt.
Hoe werkt het?
• Prestatiebeurs: Dit is een gift die je NIET terug hoeft te betalen (ca. €1.000-1.300/maand afhankelijk van woonsituatie)
• Aanvullende beurs: Extra geld als je ouders weinig verdienen (niet iedereen krijgt dit)
• DUO-lening: Eventueel lenen tegen lage rente; je begint terug te betalen na je studies

Praktische voorbeelden:
• Thuiswonend MBO'er: ~€1.000/maand prestatiebeurs
• Uitwonend MBO'er: ~€1.300/maand prestatiebeurs
• Met bijbaan en hoog inkomen: misschien minder of niets (DUO kijkt naar je verdiensten!)

Belangrijke deadlines:
• Vraag VOOR 1 juli aan voor augustus uitbetaling
• Check je aanvraag regelmatig in Mijn DUO
• Meld wijzigingen direct (bijbaan, verhuizing, enz.)`,
    completed: true,
    quickTips: ['Vraag vóór 1 juli aan via Mijn DUO voor augustus', 'Check of je recht hebt op aanvullende beurs', 'Meld ALLE inkomsten (bijbaan, stagevergoeding)', 'Bijhouden hoe je geld uitgeeft helpt voor later'],
    faqs: [
      { question: 'Hoe lang duurt een aanvraag bij DUO?', answer: 'Meestal 1-2 werkdagen, maar rond augustus kan het 2-3 weken duren. Vraag daarom vroeg aan!' },
      { question: 'Moet ik elk jaar opnieuw aanvragen?', answer: 'Nee, maar je moet je situatie checken elk schooljaar in Mijn DUO. Wijzigingen in opleiding, werk of woonstatus moeten je direct melden!' },
      { question: 'Wat als ik veel verdien met bijbaan?', answer: 'DUO telt je inkomsten mee. Te veel bijverdienen kan betekenen dat je minder studiefinanciering krijgt. Dus check je limieten op duo.nl!' },
      { question: 'Kan ik studiefinanciering en bijbaan combineren?', answer: 'Ja! Maar je mag niet te veel verdienen (rond €56 per maand limiet voor "student-werk"). Check actuele bedragen op DUO.' },
      { question: 'Wat als ik mijn opleiding verander?', answer: 'Meld dit direct bij DUO. Je studiefinanciering kan stopgezet of aangepast worden. Uitstel aanvragen is soms beter dan stoppen!' },
      { question: 'Hoe betaal ik mijn DUO-schuld terug?', answer: 'Terugbetaling start ca. 2 jaar na je studies. Je betaalt alleen terug als je genoeg verdient. Check je schuld in Mijn DUO en bespreek mogelijkheden als het moeilijk wordt.' }
    ],
    quiz: {
      question: 'Je begint een MBO-opleiding en woont thuis. Wanneer kun je studiefinanciering aanvragen?',
      correctAnswer: 1,
      options: ['Als je 17 bent en je school inschrijft', 'Als je 18 bent en ingeschreven staat', 'Pas aan het eind van je eerste jaar'],
      explanation: 'Correct! Je moet 18 zijn én officieel ingeschreven staan bij je school. Vraag dit een maand voor je 18e verjaardag aan via Mijn DUO zodat je geld direct krijgt als je jarig bent!'
    }
  },
  {
    title: 'OV-studentenkaart',
    anchor: 'ov-kaart',
    titleShort: 'OV',
    description: 'Reis voordelig met trein, bus en metro.',
    longDescription: `De OV-studentenkaart geeft je gratis of met korting reizen in het weekend of doordeweeks. Je kiest een product via DUO. 

Je hebt 2 opties:
• Weekend Vrij: Gratis reizen op zaterdag en zondag, doordeweeks 40% korting
• Doordeweeks korting: Doordeweeks 40% korting, weekends normale prijzen

Wie krijgt dit?
Je moet recht hebben op studiefinanciering bij DUO. Geen studiefinanciering? Dan krijg je ook geen OV-studentenkaart.

Praktisch:
• Koppel je studentenproduct aan je OV-chipkaart
• Het gaat METEEN in (of volgende maand)
• Je kan switchen tussen Weekend Vrij en doordeweeks (meestal per maand)

Waarschuwing: Vergeet NIET je product stop te zetten als je je studies afmaakt! Anders betaal je veel teveel.`,
    completed: false,
    quickTips: ['Koppel je kaart op tijd aan je OV-chipkaart', 'Kies Weekend Vrij of doordeweeks (kost je ongeveer hetzelfde)', 'Stop je product METEEN als je klaar bent', 'Check je saldo/termijn regelmatig'],
    faqs: [
      { question: 'Wanneer gaat mijn OV in?', answer: 'Meestal van de eerstvolgende maand af. Vraag het voor 15e van de maand aan en het gaat van de 1e van volgende maand in.' },
      { question: 'Hoe zet ik mijn OV-product stop?', answer: 'Ga naar de GVB loket of check Mijn DUO. Je MOET dit zelf doen; DUO stopt het niet automatisch!' },
      { question: 'Wat als ik vergeet stop te zetten?', answer: 'Dan betaal je het vol tarief. Je krijgt een flinke rekening. Zet het onmiddellijk stop als je geen recht meer hebt!' },
      { question: 'Kan ik wisselen tussen Weekend Vrij en korting?', answer: 'Ja, meestal per maand. Check op duo.nl hoe laat je de wijziging moet aanvragen voor volgende maand.' },
      { question: 'Werkt mijn OV ook in het buitenland?', answer: 'Het OV-product werkt in Nederland. Voor internationale reizen betaal je normaal tarief.' }
    ],
    quiz: {
      question: 'Je kiest Weekend Vrij. Wat betaal je?',
      correctAnswer: 1,
      options: ['Niets op zaterdag/zondag, normaal tarief doordeweeks', 'Gratis op zaterdag/zondag, 40% korting doordeweeks', 'Altijd 40% korting'],
      explanation: 'Correct! Weekend Vrij = gratis zaterdag/zondag, maar doordeweeks 40% korting (niet gratis). Ideaal als je veel in het weekend reist!'
    }
  },
  {
    title: 'Zorgverzekering & toeslagen',
    anchor: 'zorgverzekering',
    titleShort: 'Zorg',
    description: 'Verplichte zorgverzekering + zorgtoeslag.',
    longDescription: `In Nederland ben je verplicht een basiszorgverzekering af te sluiten. Als je 18 wordt, moet je zelf een polis regelen. 

Wat kost zorgverzekering?
• Basispolis: ~€150-200/maand (veel goedkoper voor jongeren)
• Praktijk: Vergelijk premies op zorgkaartnederland.nl

Zorgtoeslag = gratis geld!
• Je krijgt geld van de staat om je verzekering betaalbaarder te maken
• Je moet dit ZELF aanvragen bij de Belastingdienst (gaat niet automatisch!)
• Met zorgtoeslag betaal je soms maar €50-100/maand

Wie krijgt zorgtoeslag?
• Je moet 18+ zijn
• Je inkomen mag niet te hoog zijn (~€30.000/jaar als je alleen woont)
• Meestal krijgen MBO-studenten dit

Let op:
• Meld je inkomen op tijd (bijbaan!)
• Toeslag kan TERUG gevraagd worden als je inkomsten stijgen
• Geen toeslag? Dan betaal je het hele bedrag zelf`,
    completed: false,
    quickTips: ['Vraag zorgtoeslag DIRECT aan bij Belastingdienst', 'Meld ALLES wat je verdient (bijbaan, stage)', 'Vergelijk zorgverzekeraars op premie EN service', 'Zet herinnering: jaarlijks controleren + inkomsten melden'],
    faqs: [
      { question: 'Heb ik direct een boete als ik niet op tijd verzeker?', answer: 'Niet direct, maar je hebt een beperkte "ik ben niet verzekerd"-periode. Daarna krijg je terugwerkende premies + rente. Dus verzeker je DIRECT als je 18 bent!' },
      { question: 'Kan ik zorgtoeslag met terugwerkende kracht aanvragen?', answer: 'Ja, tot 6 maanden terug in hetzelfde kalenderjaar. Dus aanvragen is altijd de moeite!' },
      { question: 'Wat gebeurt er als ik mijn premie niet betaal?', answer: 'Na vervaldag rente en mogelijk opschorting van je dekking. Zorg dat je toeslag meteen op je rekening staat!' },
      { question: 'Hoe hoog is zorgtoeslag ongeveer?', answer: 'Afhankelijk van je inkomen, meestal €50-150/maand voor studenten. Meer info via belastingdienst.nl' },
      { question: 'Moet ik verzekerd blijven als ik stoppen met studeren?', answer: 'Ja! Je bent ALTIJD verplicht verzekerd. Zelfs als je niet studeert of werkt moet je een polis hebben.' }
    ],
    quiz: {
      question: 'Je verdient €400/maand in een bijbaan. Wat moet je doen?',
      correctAnswer: 2,
      options: ['Niets, DUO weet dit automatisch', 'Dit melden aan DUO', 'Dit melden aan de Belastingdienst (voor zorgtoeslag) EN DUO (voor studiefinanciering)'],
      explanation: 'Correct! Je moet dit aan TWEE plekken melden: Belastingdienst (zorgtoeslag) en DUO (studiefinanciering). Beiden willen je inkomsten weten!'
    }
  },
  {
    title: 'Woonkosten & huurtoeslag',
    anchor: 'woonkosten',
    titleShort: 'Wonen',
    description: 'Energiekosten, huur, en huurtoeslag.',
    longDescription: `Woonkosten zijn vaak de GROOTSTE uitgave voor jong volwassenen. Goed plannen scheelt veel stress!

Hoeveel geld heb je nodig?
• Huur: €300-800 (afhankelijk van wat/waar)
• Nutsvoorzieningen: €100-150 (gas, water, elektra)
• Internet: €20-40
• Totaal: ~€500-1000/maand

Huurtoeslag = geld van de gemeente
• Tot ~€250/maand voor studenten
• Je moet ZELF aanvragen via gemeente/SVB
• Belangrijk: je woning moet "zelfstandig" zijn (niet gedeelde keuken)

Wie krijgt huurtoeslag?
• Je bent 18+
• Je huurt een zelfstandige woning  
• Je bruto huur is minimum €350-400
• Je inkomen is laag genoeg (~studiefinanciering = vaak volstaat)

Praktische tips:
• Zoekopdracht: Funda, Kamernet, Woonpioniers
• Huisbazen willen inschrijving + referentie
• Sluit geen overeenkomst zonder voorwaarden te lezen
• Budget: huur + utilities + verzekering + voedsel`,
    completed: false,
    quickTips: ['Bereken ALLE woonkosten voor je zoekt', 'Vraag huurtoeslag aan (kan tot €250/maand zijn!)', 'Zorg dat je een werkcontract/inschrijving hebt voor de huisbaas', 'Sluit woning- en inboedelverzeking af'],
    faqs: [
      { question: 'Kan ik huurtoeslag krijgen voor een gedeelde woning?', answer: 'Helaas niet voor gedeelde keukens. Je woning moet zelfstandig zijn (eigen keuken, badkamer etc).' },
      { question: 'Hoeveel huurtoeslag krijg ik?', answer: 'Verschilt per gemeente. Ruwweg: je huur - 20% = je bijdrage. Rest betaalt gemeente (max ~€250). Check je gemeente!' },
      { question: 'Welke documenten heb ik nodig?', answer: 'Huurcontract, proof of income (DUO brief), bankgegevens, ID. Elke gemeente vraagt iets anders; bel de SVB.' },
      { question: 'Kan een MBO-student huurtoeslag krijgen?', answer: 'Ja! Als je recht hebt op studiefinanciering en een zelfstandige woning huurt, meestal wel. Check je gemeente!' },
      { question: 'Wat als huisbaas geen toeslagformulier wil ondertekenen?', answer: 'Dit is standaard; leg uit dat je toeslag krijgt (huisbaas krijgt zekerheid dat jij kan betalen). Blijf kalm en vriendelijk.' }
    ],
    quiz: {
      question: 'Je huurt een kamer met gedeelde keuken voor €350/maand. Kun je huurtoeslag krijgen?',
      correctAnswer: 1,
      options: ['Ja, zolang je huur onder €500 ligt', 'Nee, gedeelde keukens tellen niet mee', 'Ja, maar alleen het deel van de huur'],
      explanation: 'Helaas: huurtoeslag is voor zelfstandige woningen. Gedeelde keukens/badkamers tellen niet mee. Zoek een kamer met eigen keukentte!'
    }
  },
  {
    title: 'Belangrijke documenten',
    anchor: 'documenten',
    titleShort: 'Papieren',
    description: 'ID, DigiD, bankrekening en meer.',
    longDescription: `Een eigen huishouden beginnen stelt vragen. Zorg dat je deze zaken goed geregeld hebt:

Je MOET hebben:
1. Geldig ID-bewijs (paspoort of ID-kaart)
   - Aanvraag: GBA/gemeente ~4-6 weken
   - Kosten: €50-75
   
2. DigiD (digitale identiteit voor overheid)
   - Nodig voor: DUO, Belastingdienst, SVB, gemeente
   - Hoe: digiD.nl (snel + gratis)
   - Zet 2-factor-auth AAN (SMS-verificatie)!

3. Eigen bankrekening (bij 18 jaar)
   - Kiezen: reguliere bank, juniorenrekening, online bank
   - Gratis voor jongeren (meestal)
   - Nodig voor: DUO-uitbetaling, toeslag, huurrente
   
4. BSN-gegevens (Burgerservicenummer)
   - Dit krijg je automatisch van gemeente
   - NOOIT delen met onbekenden!
   - Zet in veilige plek

Documenten digitaal opslaan:
• Foto van ID/paspoort (beveiligd)
• Digitale DigiD back-up codes (BELANGRIJK!)
• Huurcontract (PDF)
• DUO-brieven (screenshots)
• Bankrekening-gegevens (veilig)

Waarschuwing:
• Zet NOOIT je BSN/volledige ID online
• Delen in chat/social media = identiteitsfraude risico!
• Gebruik sterke wachtwoorden + 2FA overal`,
    completed: false,
    quickTips: ['Zet DigiD 2FA (SMS) AAN zodra je het hebt', 'Sla ID-foto veilig op (niet in WhatsApp!)', 'Maak back-up van DigiD codes en sla veilig op', 'Check elk 6 maanden: zijn al je abonnementen/rekeningen correct?'],
    faqs: [
      { question: 'Welke documenten mag ik delen in de WatNu18 chat?', answer: 'GEEN vertrouwelijke gegevens! Geen BSN, bankgegevens, volledige ID-foto, paspoort. Chat alleen over vragen, niet over persoonsgegevens!' },
      { question: 'Waar kan ik mijn DigiD-codes veilig bewaren?', answer: 'Print ze uit en leg in een gesloten map thuis. Of sla op in een beveiligde wachtwoordmanager (bijv. Bitwarden, 1Password).' },
      { question: 'Hoe activeer ik mijn eigen bankrekening?', answer: 'Ga naar je bank met ID + DigiD. Meestal online activering. Duurt 5-10 minuten. Meeste banken geven IBAN direct.' },
      { question: 'Kan ik mijn ID-kaart online aanvragen?', answer: 'Nee, je moet naar de gemeente. Wél kan je online een afspraak maken om tijd te besparen.' },
      { question: 'Wat als ik mijn DigiD kwijt ben (wachtwoord)?', answer: 'Ga naar logmein.digid.nl → "Ik ben mijn gegevens kwijt" → volg stappen. Je kan je DigiD herstellen via SMS.' }
    ],
    quiz: {
      question: 'Je hebt je DigiD-wachtwoord vergeten. Wat doe je?',
      correctAnswer: 0,
      options: ['Ga naar logmein.digid.nl en herstellen via SMS', 'Bel de gemeente', 'Maak een nieuwe DigiD aan'],
      explanation: 'Correct! Ga naar logmein.digid.nl en volg "Ik ben mijn wachtwoord kwijt". Je krijgt een SMS-code en kan het herstellen. Geen gemeente nodig!'
    }
  },
  {
    title: 'HBO-doorstroom & rechten',
    anchor: 'hbo-doorstroom',
    titleShort: 'HBO →',
    description: 'Wat gebeurt er met studiefinanciering bij doorstroom naar HBO?',
    longDescription: `Proficiat! Je MBO af en gaat naar HBO? Goed nieuws: veel regelt DUO soepel.

Studiefinanciering bij HBO-doorstroom:
• Je prestatiebeurs gaat DOOR
• Soms krijg je EXTRA beurs voor HBO (ondernemingsfonds!)
• Je lening kan je meenemen naar HBO
• Je hoeft niet opnieuw aan te vragen (DUO ziet je inschrijving)

Hoe zit dat precies?
1. Je bent ingeschreven bij HBO-school
2. DUO ziet dit automatisch (meestal via Studiefinanciering register)
3. Je prestatiebeurs/toeslag wordt doorgezet
4. Mogelijk studiefinanciering VERHOGING voor HBO-traject

Termijnen en aandachtspunten:
• Meld je HBO-inschrijving in Mijn DUO
• Kijk goed: sommige HBO's hebben flexibel ingangsmoment (bijv. januari)
• Als je pauze neemt tussen MBO en HBO: meld dit aan DUO!
• Korting/beurs stopt als je langer dan 1 maand pauze hebt

Wat met je schuld?
• De lening die je hebt opgebouwd GAAT MEEMET JE
• Je start NIET opnieuw (je schuld wordt niet kwijtgescholden)
• Terugbetaling begint pas 2 jaar NADAT je HBO afmaakt

Financieel voordeel:
MBO + HBO = meer studiefinanciering ≈ extra €6.000-12.000! Dit kan helpen om je schuld af te betalen.`,
    completed: false,
    quickTips: ['Zorg dat je HBO-inschrijving in Mijn DUO staat', 'Wacht niet tot HBO start: check 2 maanden van tevoren', 'Let op: langer dan 1 maand pauze = toeslag stopt', 'Vraag DUO specifiek welke beurs je krijgt voor HBO'],
    faqs: [
      { question: 'Wat als ik na MBO eerst ga werken, dan HBO?', answer: 'Dan stopt je studiefinanciering. Als je later terugkomt naar school, kun je ergens opnieuw aanvragen. Meld pauzes lang van tevoren!' },
      { question: 'Krijg ik meer geld voor HBO dan voor MBO?', answer: 'Soms! HBO-niveau kan meer beurs opleveren (ca. €100-200 extra/maand). Vraag dit proactief in Mijn DUO.' },
      { question: 'Hoe lang mag ik pauze hebben tussen MBO en HBO?', answer: 'Tot ~1 maand zonder dat je toeslag stopt. Langer = duidelijk afgesproken pauze. Meld het direct!' },
      { question: 'Verandert mijn huurtoeslag bij HBO?', answer: 'Nee, huurtoeslag check je inkomen/huur, niet je scholingsniveau. Je kan dezelfde huurtoeslag houden.' },
      { question: 'Wat als mijn MBO-schuld heel hoog is?', answer: 'HBO geeft extra studiefinanciering, maar dit gaat NIET naar je schuld af. Dit is je inkomsten. Je moet zelf bijverdienen/bezuinigen om af te lossen.' }
    ],
    quiz: {
      question: 'Je bent klaar met MBO en start in september HBO. Wat moet je doen?',
      correctAnswer: 1,
      options: ['Wachten tot september en dan aanvragen', 'In juli je HBO-inschrijving in Mijn DUO controleren en DUO bellen', 'Niets, DUO ziet dit automatisch'],
      explanation: 'Best is: check in Mijn DUO dat je HBO-inschrijving daar staat. Bel DUO als het niet klopt. DUO ziet het NIET altijd meteen. Beter voorkomen dan later zonder geld zitten!'
    }
  },
  {
    title: 'Stoppen, overstappen & schuld',
    anchor: 'stoppen-overstappen',
    titleShort: 'Stop/Schuld',
    description: 'Wat gebeurt er met je schuld & studiefinanciering als je stopt?',
    longDescription: `Soms werkt een opleiding niet uit. Of je vindt wat anders. Wat gebeurt er dan met je studiefinanciering en schuld?

Scenario 1: Je stopt NA je eerste jaar
• De prestatiebeurs die je hebt gekregen? **Je hoeft die NIET terug te betalen (het is een gift!)
• De DUO-lening die je hebt opgenomen? **Die moet je WEL teruebetalen
• Recht op studiefinanciering stopt per direct
• Schuld: ruwweg €6.000-12.000 (afhankelijk van wat je hebt opgenomen)

Scenario 2: Je onderbreekt je opleiding (pauze van 6 maanden)
• Je studiefinanciering STOPT
• Je schuld GROEIT NIET (je leent niet meer)
• Terugekomst? Meld dit aan DUO en start opnieuw
• Voordeel: je schuld wordt niet hoger

Scenario 3: Je wisselt van opleiding (bijv. ander MBO-traject)
• Check of BEIDE opleidingen "erkend" zijn bij DUO
• Je studiefinanciering GAAT DOOR
• Schuld: dezelfde (je stapelt niet dubbel op)
• Belangrijk: meld wisselingmeteen in Mijn DUO

Terugbetaling van DUO-lening:
• Je begint terug te betalen 2 jaar NADAT je studie eindigt
• Je betaalt % van je inkomen (flexibel!)
• Minimum: ~€50/maand
• Geen inkomen? Dan betaal je NIETS (voorwaarden gelden!)

Wat je MOET doen als je stopt:
1. Meld dit DIRECT bij DUO (chat/telefoon/Mijn DUO)
2. Vraag om pauze-verlenging (als je even uit wilt)
3. Vraag hoeveel schuld je hebt (check je voorspelling)
4. Plan: hoe ga je terugbetalen? (werken, besparen, schuldhulp)
5. Controleer: stopt je OV-kaart? Stop het zelf!

Schuldhulpverlening:
Als je schuld groot voelt: 
• Schuldhulpmaatschappij kan helpen (gratis!)
• Bel: 030-2360360 of mail: schuldhulp.nl
• Ze helpen je een betalingsregeling te maken
• Je bent NIET alleen!`,
    completed: false,
    quickTips: ['Stoppen? Meld DUO METEEN (niet later!)', 'Stop je OV-product zelf (duurt 2 seconden)', 'Check je schuldbedrag in Mijn DUO', 'Schuldhulp is gratis en vertrouwelijk', 'Pauze van 6 maanden = schuld stopt met groeien'],
    faqs: [
      { question: 'Moet ik de prestatiebeurs terugbetalen als ik stop?', answer: 'Nee! Prestatiebeurs is een gift. Alleen DUO-lening moet je terug betalen. Checken: wat je kreeg (prestatie vs lening) in Mijn DUO.' },
      { question: 'Hoe snel groeit mijn schuld als ik stop?', answer: 'Direct! Als je stopt en je lening nog actief is, kan het nog even doorlopen. Daarom: meld DIRECT aan DUO.' },
      { question: 'Kan ik mijn schuld kwijtschelden?', answer: 'Normaal niet. MAAR: als je geweldige omstandigheden hebt (ziekte, werkloosheid), kan schuldhulp helpen. Ga niet zelf weg: vraag hulp!' },
      { question: 'Wat if ik na 1 jaar teruicom?', answer: 'Meld je direct TERUG in Mijn DUO. Je schuld van vorig jaar gaat mee. Je krijgt nieuwe studiefinanciering als je voldoet aan voorwaarden.' },
      { question: 'Hoeveel rente betaal ik op mijn schuld?', answer: 'DUO-lening: ca. 0% rente (of beleid-afhankelijk). Check duo.nl voor actueel %! Klein voordeel: je schuld groeit niet door rente.' },
      { question: 'Kan ik versneld terugbetalen?', answer: 'Ja! Je kan extra betalen zonder straf. Hoe sneller je betaalt, hoe minder schuld totaal. Handig als je goed verdient!' }
    ],
    quiz: {
      question: 'Je stopt voortijdig met MBO. Jij hebt €8.000 prestatiebeurs ontvangen en €12.000 geleend. Wat moet je terugbetalen?',
      correctAnswer: 1,
      options: ['Alles: €20.000', 'Alleen de lening: €12.000', 'Niets, het is onderwijs'],
      explanation: 'Je moet alleen de €12.000-lening terugbetalen! Prestatiebeurs is een GIFT. Dit is een groot voordeel van DUO. Werk snel het geleende geld af!'
    }
  }
])

const extraFaqs = [
  { question: 'Kan ik studiefinanciering en bijbaan combineren?', answer: 'Ja! Maar je mag niet te veel verdienen. Check je limieten op duo.nl. Veel MBO\'ers werken ~12 uur/week naast studiefinanciering. Zolang je je inkomen meldt, is het prima.' },
  { question: 'Moet ik zorgtoeslag terugbetalen als mijn inkomen stijgt?', answer: 'Ja, dat kan. Pas je inkomen OP TIJD aan bij de Belastingdienst. Hoe eerder je meldt, hoe minder je terug hoeft te betalen. Draai je claim niet om later!' },
  { question: 'Wat regel ik eerst als ik bijna 18 ben?', answer: 'Timeline: 3 maanden voor verjaardag: ID-aanvraag → 2 maanden voor: DigiD + bankrekening → 1 maand voor: DUO-aanvraag + zorgtoeslag. Zo heb je geld klaar als je jarig bent!' },
  { question: 'Wat als mijn ouders me niet kunnen helpen met formulieren?', answer: 'Geen probleem! School heeft begeleiding, jongerenloket helpt gratis, en DUO.nl heeft stappenplannen. Video-tutorials op YouTube helpen ook. Je bent niet alleen!' },
  { question: 'Ik heb al 18 maar nog niets aangevraagd. Is het te laat?', answer: 'Nee, NOOIT te laat! Je kan studiefinanciering altijd terugwerkend aanvragen (max 6 maanden). Dus aanvragen nu! Zorgtoeslag ook. Beter laat dan nooit.' },
  { question: 'Wat als mijn ouders veel verdienen? Krijg ik nog geld?', answer: 'Ja! Zelfs met rijke ouders krijg je prestatiebeurs. Aanvullende beurs hangt van hun inkomen af, maar je basis krijg je altijd. Win-win!' },
  { question: 'Hoeveel schuld heb ik na 4 jaar MBO + HBO?', answer: 'Ruwweg: MBO 4 jaar = €12.000-16.000 schuld (prestatiebeurs telt niet!). HBO 4 jaar = extra €12.000-16.000. MAAR: HBO geeft extra beurs (ca. €300/maand). Dus schuld valt mee!' },
  { question: 'Kan ik gaten in mijn studie opvullen met DUO?', answer: 'Als je een erkende opleiding doet: ja. Bijscholing? Nee. Check duo.nl welke vakken/certificaten tellen. Betaald uit je prestatiebeurs-potje.' }
]

const completedCount = computed(() => features.value.filter(f => f.completed).length)
const overallProgress = computed(() => {
  return Math.round((completedCount.value / features.value.length) * 100)
})
const journeyPoints = computed(() => completedCount.value * 120)
const nextIncompleteTitle = computed(() => {
  const next = features.value.find(f => !f.completed)
  return next ? next.titleShort : 'Alles afgerond'
})

function scrollToFeatures() {
  navigateTo('#features')
}

function selectFeature(index) {
  selectedFeature.value = index
  expandedFaqs.value = false
  resetQuiz()
  nextTick(() => {
    document.querySelector('.details')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  })
}

function navigateTo(raw) {
  if (typeof window === 'undefined') return
  const normalized = (raw || '').trim()
  const withHash = normalized.startsWith('#') ? normalized : `#${normalized}`
  const id = withHash === '#' ? '' : withHash.slice(1)

  if (!id || id === 'top') {
    selectedFeature.value = null
    nextTick(() => {
      document.getElementById('top')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    })
    try {
      history.replaceState(null, '', `${window.location.pathname}${window.location.search}`)
    } catch {
      /* ignore */
    }
    return
  }

  const featureIndex = features.value.findIndex((f) => f.anchor === id)
  if (featureIndex >= 0) {
    selectFeature(featureIndex)
    try {
      history.replaceState(null, '', `#${id}`)
    } catch {
      /* ignore */
    }
    return
  }

  selectedFeature.value = null
  const el = document.getElementById(id)
  if (el) {
    nextTick(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }))
    try {
      history.replaceState(null, '', `#${id}`)
    } catch {
      /* ignore */
    }
  }
}

provide(siteNavigationKey, navigateTo)

function submitQuizAnswer(answerIndex) {
  if (!features.value[selectedFeature.value].quiz) return
  currentQuizAnswer.value = answerIndex
  const quiz = features.value[selectedFeature.value].quiz
  const isCorrect = answerIndex === quiz.correctAnswer
  quizAttempted.value = true
  quizResult.value = { isCorrect, explanation: quiz.explanation }
  if (isCorrect) {
    features.value[selectedFeature.value].completed = true
    setTimeout(() => {
      selectedFeature.value = null
    }, 5000)
  }
}

function resetQuiz() {
  currentQuizAnswer.value = null
  quizResult.value = null
  quizAttempted.value = false
}

function retryQuiz() {
  resetQuiz()
}

function scrollFeatureRail(direction) {
  if (!featureRail.value) return
  const amount = Math.max(320, featureRail.value.clientWidth * 0.85)
  featureRail.value.scrollBy({ left: direction * amount, behavior: 'smooth' })
}

function applySavedProgress() {
  if (typeof window === 'undefined') return
  const raw = window.localStorage.getItem(PROGRESS_STORAGE_KEY)
  if (!raw) return
  try {
    const parsed = JSON.parse(raw)
    if (!Array.isArray(parsed)) return
    features.value = features.value.map((feature, idx) => ({
      ...feature,
      completed: Boolean(parsed[idx]),
    }))
  } catch {
    // Ignore invalid localStorage payloads.
  }
}

onMounted(() => {
  applySavedProgress()
  const hash = window.location.hash
  if (hash && hash.length > 1) {
    nextTick(() => navigateTo(hash))
  }
})

watch(
  () => features.value.map(f => f.completed),
  (progressState) => {
    if (typeof window === 'undefined') return
    window.localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(progressState))
  },
  { deep: true }
)

</script>

<style>
@import './styles/variables.css';

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-family-base);
  font-size: var(--font-size-base);
  line-height: var(--line-height-normal);
  color: var(--color-gray-100);
  background-color: var(--color-black);
  background-image:
    radial-gradient(120% 90% at 8% 4%, rgba(25, 68, 49, 0.5) 0%, transparent 48%),
    radial-gradient(70% 65% at 88% 14%, rgba(96, 113, 101, 0.8) 0%, transparent 52%),
    radial-gradient(90% 80% at 50% 100%, rgba(20, 39, 24, 0.7) 0%, transparent 55%),
    radial-gradient(50% 70% at 50% 50%, rgba(44, 78, 58, 0.7) 0%, transparent 55%),
    linear-gradient(180deg, #0f2d0b 0%, #0f290f 45%, #152a1a 100%);
  background-attachment: fixed;
  position: relative;
  overflow-x: hidden;
}

body::before {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: -2;
  background-image:
    linear-gradient(rgba(34, 255, 0, 0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgb(255 255 255 / 5%) 1px, transparent 1px),
    radial-gradient(circle at 50% 50%, rgb(255 255 255 / 6%) 0 1px, transparent 1px);
  background-size: 56px 56px, 56px 56px, 112px 112px;
  background-position: center, center, 28px 28px;
  opacity: 0.35;
}

body::after {
  content: '';
  position: fixed;
  inset: -12%;
  pointer-events: none;
  z-index: -1;
  background:
    radial-gradient(circle at 14% 24%, rgb(81, 109, 90) 0 150px, transparent 170px),
    radial-gradient(circle at 70% 84%, #3b653f 0 180px, transparent 205px),
    radial-gradient(circle at 22% 28%, rgba(40, 92, 68, 0.28) 0%, transparent 34%),
    radial-gradient(circle at 78% 72%, rgba(50, 91, 62, 0.22) 0%, transparent 32%);
  opacity: 0.5;
  animation: ambientGlow 155s ease-in-out infinite alternate;
}

.lower-half {
  background: var(--color-gray-100);
  padding: var(--spacing-3xl) var(--spacing-xl);
  height: 100%;
  width: 100%;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  /* Keeps hero/footer visually consistent if body backgrounds ever fail to paint */
  background: transparent;
}

@keyframes fillCard {
  from {
    background: white;
  }
  to {
    background: var(--color-accent-alt-1);
  }
}

@keyframes fillCardB {
  from {
    background: var(--color-bg-lightest);
  }
  to {
    background: var(--color-accent-alt-1);
  }
}

@keyframes ambientGlow {
  0% {
    transform: translate3d(-0.15%, -0.345%, 0) scale(1);
  }
  100% {
    transform: translate3d(0.15%, 0.345%, 0) scale(1.06);
  }
}

.main-content {
  flex: 1;
  max-width: 100%;
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xl);
}

.progress-banner {
  width: 100%;
  max-width: 100%;
  background-color: var(--color-white);
  padding: var(--spacing-xl) var(--spacing-2xl);
  color: var(--color-primary);
  box-shadow: var(--shadow-lg);
}

.progress-content {
  max-width: var(--container-width);
  margin: 0 auto;
}

/* Sticky header offset for in-page links */
#top,
#features,
#faq,
#half,
#social,
.feature-card[id] {
  scroll-margin-top: 5.5rem;
}

.progress-text h3 {
  font-size: var(--font-size-xl);
  margin-bottom: var(--spacing-xs);
}

.progress-text p {
  opacity: 0.9;
  margin-bottom: var(--spacing-md);
}

.journey-meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-md);
}

.journey-pill {
  background: rgba(0, 0, 0, 0.1);
  border-radius: var(--radius-full);
  padding: 6px 12px;
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-semibold);
}

.progress-bar {
  height: 8px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: var(--radius-full);
  overflow: hidden;
  margin-bottom: var(--spacing-lg);
}

.progress-fill {
  height: 100%;
  background: var(--color-accent-alt);
  border-radius: var(--radius-full);
  transition: width 0.3s ease;
}

.progress-items {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-sm);
  justify-content: space-between;
}

.progress-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  background: rgba(0, 0, 0, 0.1);
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--radius-full);
  font-size: var(--font-size-xs);
  backdrop-filter: blur(4px);
}

.progress-item.done {
  background: var(--color-success);
}

.icon {
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.2);
  border-radius: var(--radius-full);
  font-size: 12px;
}

.hero {
  padding: var(--spacing-3xl) var(--spacing-2xl);
}

.hero-content {
  max-width: var(--container-width);
  margin: 0 auto;
}

.hero-title {
  font-size: var(--font-size-5xl);
  font-weight: 800;
  color: var(--color-white);
  line-height: 1.2;
  margin-bottom: var(--spacing-lg);
}

.hero-title span {
  color: var(--color-accent);
}

.hero-subtitle {
  font-size: var(--font-size-lg);
  color: var(--color-gray-300);
  max-width: 640px;
  margin-bottom: var(--spacing-2xl);
}

.cta-btn {
  background: linear-gradient(135deg, var(--color-cta), var(--color-cta-dark));
  border: none;
  padding: var(--spacing-md) var(--spacing-2xl);
  border-radius: var(--radius-full);
  font-weight: var(--font-weight-bold);
  color: white;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  font-size: var(--font-size-base);
}

.cta-btn:hover {
  transform: translateY(1px);
  box-shadow: var(--shadow-lg);
}

.features-wrapper {
  max-width: var(--container-width);
  margin: 0 auto;
}

.features {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
  padding: 0;
}

.section-header {
  text-align: center;
  margin-bottom: var(--spacing-3xl);
}

.section-header h2 {
  font-size: var(--font-size-3xl);
  color: var(--color-black);
  margin-bottom: var(--spacing-sm);
  font-weight: bolder;
}

.section-header p {
  color: var(--color-gray-800);
  max-width: 740px;
  margin: 0 auto;
  font-size: var(--font-size-lg);
  font-weight: bold;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: var(--spacing-xl);
}

.feature-card {
  background: var(--color-white);
  color: var(--color-gray-800);
  border-radius: var(--radius-sm);
  padding: var(--spacing-xl);
  border: 1px solid #000000;
  transition: all 0.25s;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.feature-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-accent);
  animation: fillCardB 0.4s ease both;
}

.feature-card.completed {
  border-left: 10px solid var(--color-success);
}

.feature-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-md);
}

.feature-header .feature-step {
  margin-bottom: 0;
}

.feature-rail-controls {
  display: none;
  justify-content: flex-end;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-md);
}

.rail-btn {
  border: 1px solid var(--color-gray-300);
  background: var(--color-white);
  border-radius: var(--radius-full);
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.feature-step {
  display: inline-flex;
  width: 36px;
  height: 36px;
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-full);
  align-items: center;
  justify-content: center;
  font-weight: bold;
  margin-bottom: var(--spacing-md);
}

.feature-badge {
  background: var(--color-success);
  font-size: var(--font-size-xs);
  padding: 2px 8px;
  border-top-right-radius: var(--radius-full);
  border-bottom-right-radius: var(--radius-full);
  color: white;
}

.feature-card h3 {
  margin: var(--spacing-md) 0 var(--spacing-sm);
  font-size: var(--font-size-xl);
}

.feature-btn {
  width: 100%;
  margin-top: var(--spacing-md);
  background: var(--color-primary);
  color: white;
  border: none;
  padding: var(--spacing-sm);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: background 0.2s;
}

.feature-btn:hover {
  background: var(--color-primary-dark);
}

.feature-highlights {
  margin: var(--spacing-md) 0 0 var(--spacing-lg);
  display: grid;
  gap: var(--spacing-sm);
  font-size: var(--font-size-sm);
  flex-grow: 1;
}

.feature-highlights li {
  color: var(--color-gray-700);
  line-height: var(--line-height-normal);
}

.details {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  color: var(--color-primary);
  padding: var(--spacing-3xl) var(--spacing-xl);
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.details-container {
  max-width: 800px;
  margin: 0 auto;
  background: var(--color-white);
  border-radius: var(--radius-md);
  color: var(--color-primary);
  padding: var(--spacing-3xl);
  box-shadow: var(--shadow-2xl);
  animation: slideUp 0.3s ease;
  max-height: 90vh;
  overflow-y: auto;
}

@keyframes slideUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.close-btn {
  background: none;
  border: none;
  color: var(--color-black);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-2xl);
  cursor: pointer;
  padding: 0;
  font-size: var(--font-size-base);
}

.details-content {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xl);
}

.details-content h2 {
  font-size: var(--font-size-2xl);
  margin-bottom: var(--spacing-md);
}

.details-content p {
  line-height: var(--line-height-relaxed);
  white-space: pre-line;
}

.details-quiz {
  background: var(--color-gray-100);
  padding: var(--spacing-2xl);
  color: var(--color-primary);
  border-radius: var(--radius-xs);
  margin-top: var(--spacing-2xl);
  border-top: 2px solid var(--color-gray-200);
  padding-top: var(--spacing-2xl);
}

.details-quiz h3 {
  margin-bottom: var(--spacing-lg);
}

.detail-faq {
  margin-top: var(--spacing-2xl);
  border-top: 2px solid var(--color-gray-200);
  padding-top: var(--spacing-xl);
}

.faq-toggle-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  background: none;
  border: none;
  cursor: pointer;
  padding: var(--spacing-md) 0;
  margin-bottom: var(--spacing-md);
  transition: color 0.2s;
}

.faq-toggle-btn:hover {
  color: var(--color-accent);
}

.faq-toggle-btn h3 {
  margin: 0;
  font-size: var(--font-size-lg);
  text-align: left;
}

.toggle-arrow {
  display: inline-flex;
  font-size: 14px;
  transition: transform 0.3s ease;
  color: var(--color-primary);
  margin-left: var(--spacing-md);
  flex-shrink: 0;
}

.toggle-arrow.expanded {
  transform: rotate(180deg);
}

.toggle-arrow:hover {
  color: var(--color-accent);
}

.faq-list {
  display: grid;
  gap: var(--spacing-lg);
  margin-top: var(--spacing-md);
  animation: expandCollapse 0.3s ease forwards;
}

@keyframes expandCollapse {
  from {
    opacity: 0;
    max-height: 0;
    overflow: hidden;
  }
  to {
    opacity: 1;
    max-height: 1000px;
    overflow: visible;
  }
}

.faq-item {
  background: var(--color-bg-lightest);
  border: 1px solid var(--color-gray-200);
  padding: var(--spacing-lg);
  border-radius: var(--radius-md);
}

.faq-item h4 {
  margin-bottom: var(--spacing-sm);
  font-size: var(--font-size-base);
}

.faq-item p {
  line-height: var(--line-height-relaxed);
  font-size: var(--font-size-sm);
}

.quiz-question {
  margin-bottom: var(--spacing-lg);
}

.quiz-question p {
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-lg);
  font-size: var(--font-size-base);
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
}

.quiz-option {
  display: block;
  width: 100%;
  text-align: left;
  background: var(--color-gray-200);
  padding: var(--spacing-md) var(--spacing-lg);
  border: solid 1px;
  border-color: var(--color-gray-300);
  border-radius: var(--radius-md);
  cursor: pointer;
  color: var(--color-primary);
  transition: all 0.2s;
  font-size: var(--font-size-sm);
}

.quiz-option:hover:not(:disabled) {
  background: var(--color-accent-light);
  border-color: var(--color-accent);
}

.quiz-feedback {
  display: flex;
  gap: var(--spacing-lg);
  padding: var(--spacing-lg);
  border-radius: var(--radius-lg);
  margin: var(--spacing-lg) 0;
}

.quiz-feedback.correct {
  background: var(--color-success-light);
  color: var(--color-primary);
  border-left: 4px solid var(--color-success);
}

.quiz-feedback.incorrect {
  background: var(--color-warning-light);
  color: var(--color-primary);
  border-left: 4px solid var(--color-warning-dark);
}

.feedback-icon {
  font-size: 2rem;
}

.quiz-action-btn {
  width: 100%;
  padding: var(--spacing-sm);
  color: var(--color-primary);
  border: none;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
}

.quiz-action-btn.retry {
  background: var(--color-warning);
  color: var(--color-primary);
}

.quiz-action-btn.completed {
  background: var(--color-success);
  color: var(--color-primary);
  cursor: default;
}

.info-section {
  padding: var(--spacing-3xl) var(--spacing-xl);
  background: var(--color-white);
  border-top: 1px solid var(--color-gray-200);
  border-bottom: 1px solid var(--color-gray-200);
}

.info-section h2 {
  text-align: center;
  font-size: var(--font-size-3xl);
  margin-bottom: var(--spacing-3xl);
  color: var(--color-white);
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--spacing-xl);
}

.info-card {
  background: var(--color-white);
  border-radius: var(--radius-lg);
  padding: var(--spacing-xl);
  text-align: center;
  color: var(--color-gray-800);
  border: 1px solid var(--color-gray-200);
  transition: all 0.2s;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  background: var(--color-accent-alt-1);
  animation: fillCard 0.4s ease both;
}

.info-icon {
  font-size: 2.5rem;
  margin-bottom: var(--spacing-md);
}

.faq-section {
  padding: var(--spacing-3xl) var(--spacing-xl);
}

.faq-section-inner {
  max-width: var(--container-width);
  margin: 0 auto;
  color: var(--color-white);
}

.faq-section-inner > p {
  color: var(--color-gray-300);
  margin: var(--spacing-sm) 0 var(--spacing-xl);
}

.faq-overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: var(--spacing-lg);
}

.faq-overview-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: var(--radius-lg);
  padding: var(--spacing-lg);
  backdrop-filter: blur(2px);
}

.stories-section {
  padding: var(--spacing-3xl) var(--spacing-xl);
  background: linear-gradient(135deg, #f0f9f4 0%, #e8f5f0 100%);
}

.stories-inner {
  max-width: var(--container-width);
  margin: 0 auto;
}

.stories-section h2 {
  text-align: center;
  font-size: var(--font-size-3xl);
  color: var(--color-primary);
  margin-bottom: var(--spacing-sm);
}

.stories-section > p {
  text-align: center;
  color: var(--color-gray-700);
  margin-bottom: var(--spacing-3xl);
}

.stories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--spacing-xl);
}

.story-card {
  background: var(--color-white);
  border-radius: var(--radius-lg);
  padding: var(--spacing-xl);
  border: 2px solid var(--color-accent-alt-1);
  text-align: center;
  color: var(--color-gray-800);
  transition: all var(--transition-base);
  box-shadow: var(--shadow-sm);
}

.story-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-accent);
}

.story-avatar {
  font-size: 3rem;
  margin-bottom: var(--spacing-md);
}

.story-card h3 {
  font-size: var(--font-size-lg);
  margin-bottom: var(--spacing-xs);
  color: var(--color-primary);
}

.story-role {
  font-size: var(--font-size-sm);
  color: var(--color-accent);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--spacing-md);
}

.story-text {
  font-size: var(--font-size-sm);
  line-height: var(--line-height-relaxed);
  margin-bottom: var(--spacing-md);
  color: var(--color-gray-700);
  font-style: italic;
}

.story-tip {
  background: var(--color-accent-alt-1);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-semibold);
  color: var(--color-primary);
  border-left: 4px solid var(--color-accent);
}

@media (max-width: 992px) {
  .feature-rail-controls {
    display: flex;
  }

  .features-grid {
    display: flex;
    overflow-x: auto;
    gap: var(--spacing-md);
    scroll-snap-type: x mandatory;
    padding-bottom: var(--spacing-sm);
  }

  .feature-card,
  .feature-card:last-child:nth-child(odd) {
    min-width: min(360px, 82vw);
    scroll-snap-align: start;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 0 var(--spacing-md);
    gap: var(--spacing-lg);
  }

  .progress-banner,
  .hero,
  .details,
  .info-section,
  .faq-section {
    padding-left: var(--spacing-lg);
    padding-right: var(--spacing-lg);
  }

  .features-wrapper {
    padding: var(--spacing-3xl) var(--spacing-md);
  }

  .hero-title {
    font-size: var(--font-size-3xl);
  }
  .progress-items {
    flex-direction: column;
    align-items: stretch;
  }
  .features-grid {
    display: flex;
    overflow-x: auto;
    gap: var(--spacing-md);
    scroll-snap-type: x mandatory;
  }

  .feature-card,
  .feature-card:last-child:nth-child(odd) {
    min-width: 88vw;
  }
}
</style>