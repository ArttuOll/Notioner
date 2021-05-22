# Notioner
Integraatio Notionin ja useiden skriptieni ja ohjelmieni välillä.

## Toiminta
Notionerilla pystyn lähettämään tietoa ohjelmista ja skripteistäni Notioniin. Käytän sitä esimerkiksi yhdessä [Finan](https://github.com/ArttuOll/FinanceAutomator) kanssa henkilökohtaisen talouteni seuraamiseen Notionissa.
Yleisemmin, Notioner vastaanottaa dataa muilta ohjelmilta, muotoilee sen Notion APIn määrittämän mukaiseksi JSON-olioksi ja lähettää sen Notioniin.

Jokaista Notionin kanssa integroitavaa ohjelmaa varten on koodattava oma moduulinsa, koska eri Notion-sivujen ja -tietokantojen rakenteet voivat olla hyvinkin erilaisia. Moduulien koko on kuitenkin hyvin pieni ja uusien tekeminen erittäin helppoa.
