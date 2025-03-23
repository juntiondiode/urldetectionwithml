import pandas as pd
import os

def download_phishing_urls():
    """
    Generate phishing URLs based on common phishing patterns
    """
    print("Preparing phishing URLs...")
    phishing_urls = [
        # Login/Account verification patterns
        "http://secure-login.facebook.com.verify-account.net",
        "https://accounts.google.com.security-check.com",
        "http://signin.amazon.account-verify.net",
        "https://paypal.com.secure-verification.org",
        "http://netflix.com.account-update.info",
        
        # Banking related
        "http://secure.banking-chase.com",
        "https://online.banking-wellsfargo.net",
        "http://secure.bankofamerica.login-verify.com",
        "https://citibank.account-secure.com",
        "http://hsbc-online.secure-access.net",
        "https://secure.banking.barclays-verify.com",
        
        # E-commerce
        "http://amazon.com.order-verify.net",
        "https://ebay.com.seller-secure.com",
        "http://alibaba.secure-transaction.net",
        "https://walmart.com.account-verify.org",
        "http://shop.aliexpress.secure-payment.com",
        
        # Social Media
        "https://facebook.password-reset.net",
        "http://instagram.verify-login.com",
        "https://twitter.account-secure.net",
        "http://linkedin.profile-verify.com",
        "https://tiktok.account-verify.net",
        "http://snapchat.login-secure.com",
        
        # Email services
        "http://gmail.password-update.com",
        "https://outlook.security-check.net",
        "http://yahoo-mail.account-verify.com",
        "https://mail.google.com.password-reset.net",
        "http://office365.email-verify.com",
        
        # Cloud services
        "https://dropbox.file-share.net",
        "http://onedrive.storage-access.com",
        "https://icloud.com.storage-verify.net",
        "http://box.com.secure-files.org",
        
        # Entertainment
        "http://netflix.subscription-renew.com",
        "https://spotify.account-verify.net",
        "http://twitch.stream-login.com",
        "https://disney-plus.account-update.com",
        "http://hulu.subscription-verify.net",
        
        # Tech companies
        "https://apple.id-verify.com",
        "http://microsoft-365.login-secure.net",
        "https://github.security-alert.com",
        "http://zoom.meeting-join.net",
        "https://adobe.license-verify.com",
        
        # Payment services
        "http://cashapp.secure-transfer.net",
        "https://venmo.payment-verify.com",
        "http://wise.money-transfer.org",
        "https://stripe.payment-process.net",
        
        # Cryptocurrency
        "http://blockchain.wallet-verify.net",
        "https://coinbase.secure-trade.com",
        "http://binance.account-verify.org",
        
        # Gaming
        "https://steam.password-reset.net",
        "http://epic-games.login-verify.com",
        "https://roblox.account-secure.net",
        
        # Shipping
        "http://fedex.tracking-verify.net",
        "https://ups.delivery-secure.com",
        "http://dhl.package-track.org",
        
        # Indian Government Services
        "http://income-tax-filing.gov.in.secure-verify.com",
        "https://aadhaar.gov.in.update-biometric.net",
        "http://passport.gov.in.application-status.org",
        "https://digilocker.gov.in.document-verify.com",
        "http://gst.gov.in.filing-secure.net",
        "https://epfo.gov.in.pension-claim.com",
        "http://india-post.gov.in.tracking-verify.net",
        "https://pan.gov.in.card-apply.org",
        "http://cowin.gov.in.vaccine-booking.com",
        "https://irctc.co.in.ticket-booking.net",
        
        # Indian Banks
        "http://onlinebanking.sbi.secure-login.net",
        "https://netbanking.hdfcbank.verify-account.com",
        "http://inetbanking.icicibank.secure-verify.org",
        "https://retail.axisbank.account-login.net",
        "http://online.yesbank.secure-access.com",
        "https://netbanking.kotak.verify-user.net",
        "http://pnbindia.secure-banking.org",
        "https://unionbankonline.account-verify.com",
        "http://canarabank.netbanking.secure.net",
        "https://online.bankofbaroda.verify-login.org",
        "http://netbanking.idbibank.secure-auth.com",
        "https://online.indianbank.account-verify.net",
        
        # UPI and Payment Apps
        "http://phonepe.secure-payment.net",
        "https://googlepay.transaction-verify.com",
        "http://paytm.wallet-recharge.org",
        "https://bhim.upi-transfer.net",
        "http://amazonpay.balance-add.com",
        
        # Additional Indian Services
        "http://uidai.gov.in.update-mobile.net",
        "https://incometax.gov.in.refund-status.org",
        "http://epfindia.gov.in.claim-status.com",
        "https://indianrail.gov.in.pnr-status.net",
        "http://post.gov.in.speedpost-track.org",
        
        # Additional Indian Banks
        "http://southindianbank.secure-login.net",
        "https://netbanking.csb.verify-account.com",
        "http://online.federalbank.secure-verify.org",
        "https://dhanlaxmi.netbanking.account-login.net",
        "http://karnatakabank.secure-access.com",
        "https://netbanking.kvb.verify-user.net",
        "http://tmbnet.secure-banking.org",
        "https://cityunionbank.account-verify.com",
        "http://dcbbank.netbanking.secure.net",
        "https://indusind.verify-login.org",
        "http://rblbank.secure-auth.com",
        "https://saraswatbank.account-verify.net",
        "http://vijayabank.secure-login.com",
        "https://lakshmivilas.netbanking.verify.net",
        
        # Kerala Government Services
        "http://kerala.gov.in.service-portal.net",
        "https://ehealth.kerala.gov.in.appointment.com",
        "http://kseb.in.bill-payment.org",
        "https://kwa.kerala.gov.in.water-bill.net",
        "http://ksrtc.in.ticket-booking.com",
        "https://keralauniversity.ac.in.result-check.net",
        "http://ktu.edu.in.exam-portal.org",
        "https://norka.kerala.gov.in.registration.com",
        "http://lsg.kerala.gov.in.tax-payment.net",
        "https://mvd.kerala.gov.in.license-verify.org",
        "http://excise.kerala.gov.in.permit-apply.com",
        "https://forest.kerala.gov.in.ecotourism.net",
        "http://agriculture.kerala.gov.in.subsidy.org",
        "https://education.kerala.gov.in.admission.com",
        
        # Kerala Local Bodies
        "http://corporation-tvm.secure-tax.net",
        "https://cochin-corporation.water-bill.com",
        "http://kozhikode-corp.property-tax.org",
        "https://kollam-corp.service-verify.net",
        
        # Additional Kerala Services
        "http://keralartc.online-booking.net",
        "https://ksebl.bill-status.com",
        "http://keralawateronline.payment.org",
        "https://akshaya.kerala.verify-service.net",
        
        # Typosquatting Patterns
        "http://kerallagov.in",  
        "http://kerela.gov.in",  
        "http://keralagovt.in",  
        "http://keralagovin.org", 
        "http://keralagov.com",  
        "http://keralaagov.in",  
        
        # Homograph Attacks (similar looking characters)
        "http://kera1a.gov.in",  
        "http://keraIa.gov.in",  
        "http://kerala.g0v.in",   
        "http://kerаla.gov.in",   
        
        # Subdomain Manipulation
        "http://gov.kerala-portal.in",
        "http://gov-in.kerala-services.com",
        "http://kerala-gov.secure-portal.in",
        "http://gov.kerala.secure-services.net",
        
        # Bank URL Patterns
        "http://sbi.secure-login.co.in",
        "http://sbi-online.secure-login.in",
        "http://online-sbi.secure-portal.com",
        "http://federaI-bank.com",  
        "http://federal.bank-login.net",
        
        # Mixed Language and Transliteration
        "http://keralasarkar.com",  
        "http://keralasarkkar.in",  
        "http://keralaservices.co.in",
        "http://keralaseva.com",    
        "http://keralasevanam.net", 
        
        # Common Misspellings
        "http://keralaonline.gov.in",
        "http://kerala-online.gov.in",
        "http://keralastate.gov.in",
        "http://keral.gov.in",      
        "http://karala.gov.in",     
        
        # Service-specific Patterns
        "http://kseb-bill.online",
        "http://ksrtc-booking.net",
        "http://kwa-bill.com",
        "http://kseb.bill-pay.net",
        "http://ksrtc.ticket-book.com",
        
        # University Patterns
        "http://ktu-results.net",
        "http://ktu.student-login.com",
        "http://keralauniv.results.net",
        "http://keralauniversity.exam-portal.com",
        
        # Local Body Patterns
        "http://tvm-corporation.com",
        "http://cochin-corp.net",
        "http://kozhikode.muncipality.org",
        "http://kollam.corp-online.com",
        
        # Certificate and Document Scams
        "http://kerala.certificate-download.com",
        "http://kerala.document-verify.net",
        "http://kerala-certificate.online",
        "http://keraladocs.verification.net",
        
        # Emergency and Time-sensitive Scams
        "http://kerala-flood-relief.org",
        "http://kerala-emergency.com",
        "http://kerala-alert.net",
        "http://kerala-warning.com",
        
        # Job and Recruitment Scams
        "http://kerala-govt-jobs.com",
        "http://kerala-recruitment.net",
        "http://kerala-vacancy.org",
        "http://kerala-employment.com",
        
        # Benefit and Welfare Scams
        "http://kerala-pension.com",
        "http://kerala-welfare.net",
        "http://kerala-scheme.org",
        "http://kerala-benefits.com",
        
        # Mobile App Related
        "http://kerala-mobileapp.com",
        "http://kerala-app-download.net",
        "http://kerala-official-app.org",
        "http://kerala-services-app.com",
        
        # HDFC Bank Phishing
        "http://hdfc-bank.secure-login.in",
        "http://hdfcbank.netbanking-login.com",
        "http://secure.hdfc-bank.co.in",
        "http://hdfcbank.login-secure.net",
        "http://netbanking-hdfc.com",
        "http://hdfc.secure-netbanking.in",
        "http://hdfcb4nk.com",                # Homograph (4 for A)
        "http://hdtcbank.com",                # Typo (t for f)
        "http://hdfcbank.com.secure-login.in", # Domain as subdomain
        "http://login.hdfc-bank.secure-portal.com",
        
        # ICICI Bank Phishing
        "http://icicibank-login.com",
        "http://icici.secure-netbanking.in",
        "http://infinity.icici-bank.co.in",
        "http://icicibank.netbanking-login.com",
        "http://secure.icici-bank.in",
        "http://icicibank.login-secure.net",
        "http://1cicibank.com",               # Homograph (1 for i)
        "http://icicibenk.com",               # Typo (e for a)
        "http://icicibank.com.secure-login.in",
        "http://infinity-icici.secure-portal.com",
        
        # Axis Bank Phishing
        "http://axis-bank.secure-login.in",
        "http://axisbank.netbanking-login.com",
        "http://secure.axis-bank.co.in",
        "http://retail.axis-bank.secure-portal.com",
        "http://ax1sbank.com",                # Homograph (1 for i)
        "http://axisbenk.com",                # Typo (e for a)
        "http://axisbank.com.secure-login.in",
        "http://login.axis-bank.secure-portal.com",
        
        # Kotak Bank Phishing
        "http://kotak.secure-netbanking.in",
        "http://kotakbank.login-secure.net",
        "http://k0tak.com",                   # Homograph (0 for o)
        "http://kotakbenk.com",               # Typo (e for a)
        "http://kotak.com.secure-login.in",
        
        # Yes Bank Phishing
        "http://yesbank.secure-login.in",
        "http://yes-bank.netbanking-login.com",
        "http://yesb4nk.com",                 # Homograph (4 for A)
        "http://yesbenk.com",                 # Typo (e for a)
        
        # Common Bank Phishing Patterns
        "http://netbanking-verify-india.com",
        "http://bank-login-secure.in",
        "http://secure-netbanking-india.com",
        "http://banking-verification.co.in",
        
        # UPI-based Phishing
        "http://upi-verification.com",
        "http://verify-upi.co.in",
        "http://upi-secure.net",
        "http://upi-validate.in",
        
        # Mobile Banking Phishing
        "http://mobilebanking-verify.com",
        "http://mobile-bank-secure.in",
        "http://bank-app-verify.com",
        "http://secure-mbanking.in",
        
        # Small Finance Bank Phishing
        "http://aubank.secure-login.in",
        "http://au-bank.netbanking-login.com",
        "http://fincare.secure-portal.in",
        "http://jana-bank.login-secure.net",
        
        # Payment Bank Phishing
        "http://airtel-bank.secure-login.in",
        "http://paytm-bank.netbanking-login.com",
        "http://jio-bank.secure-portal.in",
        "http://fino-bank.login-secure.net",
        
        # Social Engineering Patterns
        "http://bank-account-blocked.com",
        "http://kyc-update-bank.in",
        "http://bank-card-expired.com",
        "http://bank-security-alert.in",
        "http://bank-account-verify.com",
        "http://update-pan-bank.in",
        "http://bank-reward-points.com",
        "http://bank-refund-portal.in",
        
        # Emergency/Time-sensitive Bank Scams
        "http://bank-account-suspended.com",
        "http://immediate-kyc-update.in",
        "http://bank-fraud-alert.com",
        "http://urgent-card-update.in",
        
        # Bank Customer Support Scams
        "http://bank-customer-care.in",
        "http://bank-support-24x7.com",
        "http://bank-helpline-india.in",
        "http://banking-assistance.com",
        
        # Bank Offer Scams
        "http://bank-special-offer.in",
        "http://loan-approval-bank.com",
        "http://credit-card-offer.in",
        "http://bank-cashback-offer.com"
    ]
    
    return pd.DataFrame({"url": phishing_urls})

def download_legitimate_urls():
    """
    Use the provided list of legitimate URLs
    """
    print("Preparing legitimate URLs...")
    legitimate_urls = [
        # Major platforms
        "http://www.youtube.com",
        "http://www.facebook.com",
        "http://www.baidu.com",
        "http://www.yahoo.com",
        "http://www.amazon.com",
        "http://www.wikipedia.org",
        "http://www.qq.com",
        "http://www.google.co.in",
        "http://www.twitter.com",
        "http://www.live.com",
        "http://www.taobao.com",
        "http://www.bing.com",
        "http://www.instagram.com",
        "http://www.weibo.com",
        "http://www.sina.com.cn",
        "http://www.linkedin.com",
        
        # Regional domains
        "http://www.yahoo.co.jp",
        "http://www.msn.com",
        "http://www.vk.com",
        "http://www.google.de",
        "http://www.yandex.ru",
        "http://www.hao123.com",
        "http://www.google.co.uk",
        
        # News and Media
        "http://www.reddit.com",
        "http://www.cnn.com",
        "http://www.bbc.co.uk",
        "http://www.nytimes.com",
        "http://www.theguardian.com",
        "http://www.washingtonpost.com",
        "http://www.reuters.com",
        
        # E-commerce
        "http://www.ebay.com",
        "http://www.amazon.co.jp",
        "http://www.alibaba.com",
        "http://www.walmart.com",
        "http://www.target.com",
        "http://www.bestbuy.com",
        "http://www.etsy.com",
        
        # Tech
        "http://www.microsoft.com",
        "http://www.apple.com",
        "http://www.github.com",
        "http://www.stackoverflow.com",
        "http://www.gitlab.com",
        "http://www.docker.com",
        "http://www.digitalocean.com",
        
        # Cloud Services
        "http://www.dropbox.com",
        "http://www.box.com",
        "http://www.mega.nz",
        "http://www.onedrive.live.com",
        "http://www.icloud.com",
        
        # Entertainment
        "http://www.netflix.com",
        "http://www.spotify.com",
        "http://www.twitch.tv",
        "http://www.disneyplus.com",
        "http://www.hulu.com",
        "http://www.hbomax.com",
        
        # Business/Professional
        "http://www.office.com",
        "http://www.slack.com",
        "http://www.zoom.us",
        "http://www.salesforce.com",
        "http://www.hubspot.com",
        
        # Payment Services
        "http://www.paypal.com",
        "http://www.stripe.com",
        "http://www.wise.com",
        "http://www.venmo.com",
        "http://www.cashapp.com",
        
        # Cryptocurrency
        "http://www.coinbase.com",
        "http://www.binance.com",
        "http://www.kraken.com",
        "http://www.blockchain.com",
        
        # Gaming
        "http://www.steam.com",
        "http://www.epicgames.com",
        "http://www.roblox.com",
        "http://www.ea.com",
        "http://www.playstation.com",
        
        # Shipping
        "http://www.fedex.com",
        "http://www.ups.com",
        "http://www.dhl.com",
        "http://www.usps.com",
        
        # Indian Government Websites
        "http://www.india.gov.in",
        "http://www.uidai.gov.in",
        "http://www.incometax.gov.in",
        "http://www.gst.gov.in",
        "http://www.epfindia.gov.in",
        "http://www.passportindia.gov.in",
        "http://www.indianrail.gov.in",
        "http://www.indiapost.gov.in",
        "http://www.digilocker.gov.in",
        "http://www.mygov.in",
        "http://www.nsdl.gov.in",
        "http://www.epfo.gov.in",
        "http://www.nic.in",
        "http://www.irctc.co.in",
        "http://www.cowin.gov.in",
        "http://www.pan.gov.in",
        "http://www.cbic.gov.in",
        "http://www.digitalindia.gov.in",
        "http://www.meity.gov.in",
        "http://www.nrega.nic.in",
        
        # Indian Banks
        "http://www.sbi.co.in",
        "http://www.hdfcbank.com",
        "http://www.icicibank.com",
        "http://www.axisbank.com",
        "http://www.yesbank.in",
        "http://www.kotak.com",
        "http://www.pnbindia.in",
        "http://www.unionbankofindia.co.in",
        "http://www.canarabank.com",
        "http://www.bankofbaroda.com",
        "http://www.idbibank.in",
        "http://www.indianbank.in",
        "http://www.rbi.org.in",
        "http://www.federalbank.co.in",
        "http://www.iob.in",
        
        # Indian Financial Services
        "http://www.npci.org.in",
        "http://www.sebi.gov.in",
        "http://www.nabard.org",
        "http://www.sidbi.in",
        "http://www.irdai.gov.in",
        
        # Popular Indian Payment Apps/Services
        "http://www.phonepe.com",
        "http://www.paytm.com",
        "http://www.bhimupi.org.in",
        
        # Additional Indian Services
        "http://www.nps.gov.in",
        "http://www.nseindia.com",
        "http://www.bseindia.com",
        "http://www.npscra.nsdl.co.in",
        "http://www.utimf.com",
        "http://www.licindia.in",
        
        # Additional Indian Banks
        "http://www.southindianbank.com",
        "http://www.csb.co.in",
        "http://www.federalbank.co.in",
        "http://www.dhanbank.com",
        "http://www.karnatakabank.com",
        "http://www.kvb.co.in",
        "http://www.tmb.in",
        "http://www.cityunionbank.com",
        "http://www.dcbbank.com",
        "http://www.indusind.com",
        "http://www.rblbank.com",
        "http://www.saraswatbank.com",
        "http://www.vijayabank.com",
        "http://www.lvbank.com",
        "http://www.jkbank.com",
        "http://www.bandhanbank.com",
        "http://www.ujjivansfb.in",
        "http://www.aubank.in",
        "http://www.equitasbank.com",
        "http://www.finobank.com",
        
        # Kerala Government Websites
        "http://www.kerala.gov.in",
        "http://www.keralartc.com",
        "http://www.kseb.in",
        "http://www.kwa.kerala.gov.in",
        "http://www.keralauniversity.ac.in",
        "http://www.ktu.edu.in",
        "http://www.cusat.ac.in",
        "http://www.mgu.ac.in",
        "http://www.kannuruniversity.ac.in",
        "http://www.kufos.ac.in",
        "http://www.kalamandalam.org",
        "http://www.ksitm.kerala.gov.in",
        "http://www.itmission.kerala.gov.in",
        "http://www.norka.kerala.gov.in",
        "http://www.supplycokerala.com",
        "http://www.consumerfed.kerala.gov.in",
        "http://www.kserc.org",
        "http://www.ksrtc.in",
        "http://www.mvd.kerala.gov.in",
        "http://www.excise.kerala.gov.in",
        "http://www.forest.kerala.gov.in",
        "http://www.agriculture.kerala.gov.in",
        "http://www.education.kerala.gov.in",
        "http://www.lsg.kerala.gov.in",
        
        # Kerala Local Bodies
        "http://www.corporationoftrivandrum.in",
        "http://www.cochinmunicipalcorporation.kerala.gov.in",
        "http://www.kozhikodecorporation.org",
        "http://www.kollamcorporation.gov.in",
        "http://www.kochicorporation.gov.in",
        "http://www.thrissurcorporation.in",
        
        # Kerala State Services
        "http://www.keralartc.com",
        "http://www.ksfe.com",
        "http://www.ksebl.in",
        "http://www.keralawateronline.org",
        "http://www.akshaya.kerala.gov.in",
        "http://www.keltron.org",
        "http://www.ksidc.org",
        "http://www.kinfra.org",
        "http://www.kitco.in",
        "http://www.kscard.org",
        "http://www.kerafed.com",
        "http://www.matsyafed.kerala.gov.in"
        
        # State Government Portals
        # North India
        "http://www.delhi.gov.in",          # Delhi
        "http://www.haryana.gov.in",        # Haryana
        "http://www.hp.gov.in",             # Himachal Pradesh
        "http://www.jk.gov.in",             # Jammu and Kashmir
        "http://www.punjab.gov.in",         # Punjab
        "http://www.uk.gov.in",             # Uttarakhand
        "http://www.up.gov.in",             # Uttar Pradesh
        
        # Central India
        "http://www.mp.gov.in",             # Madhya Pradesh
        "http://www.cg.gov.in",             # Chhattisgarh
        
        # East India
        "http://www.wb.gov.in",             # West Bengal
        "http://www.bihar.gov.in",          # Bihar
        "http://www.jharkhand.gov.in",      # Jharkhand
        "http://www.odisha.gov.in",         # Odisha
        
        # Northeast India
        "http://www.assam.gov.in",          # Assam
        "http://www.arunachalpradesh.gov.in", # Arunachal Pradesh
        "http://www.manipur.gov.in",        # Manipur
        "http://www.meghalaya.gov.in",      # Meghalaya
        "http://www.mizoram.gov.in",        # Mizoram
        "http://www.nagaland.gov.in",       # Nagaland
        "http://www.sikkim.gov.in",         # Sikkim
        "http://www.tripura.gov.in",        # Tripura
        
        # West India
        "http://www.gujarat.gov.in",        # Gujarat
        "http://www.maharashtra.gov.in",    # Maharashtra
        "http://www.rajasthan.gov.in",      # Rajasthan
        "http://www.goa.gov.in",            # Goa
        
        # South India
        "http://www.kerala.gov.in",         # Kerala
        "http://www.karnataka.gov.in",      # Karnataka
        "http://www.tn.gov.in",             # Tamil Nadu
        "http://www.ap.gov.in",             # Andhra Pradesh
        "http://www.telangana.gov.in",      # Telangana
        
        # Union Territories
        "http://www.andaman.gov.in",        # Andaman and Nicobar
        "http://www.chandigarh.gov.in",     # Chandigarh
        "http://www.dadra.nic.in",          # Dadra and Nagar Haveli
        "http://www.daman.nic.in",          # Daman and Diu
        "http://www.lakshadweep.gov.in",    # Lakshadweep
        "http://www.puducherry.gov.in",     # Puducherry
        "http://www.ladakh.gov.in",         # Ladakh
        
        # State Cooperative Banks
        "http://www.apcoopbank.com",        # Andhra Pradesh
        "http://www.arunachalscb.com",      # Arunachal Pradesh
        "http://www.assamcoopbank.com",     # Assam
        "http://www.biharscb.com",          # Bihar
        "http://www.cgscb.com",             # Chhattisgarh
        "http://www.gscb.coop",             # Gujarat
        "http://www.harcobank.org.in",      # Haryana
        "http://www.hpscb.com",             # Himachal Pradesh
        "http://www.jkscb.com",             # Jammu and Kashmir
        "http://www.jscb.gov.in",           # Jharkhand
        "http://www.kscb.org.in",           # Karnataka
        "http://www.keralabank.com",        # Kerala
        "http://www.mpscb.com",             # Madhya Pradesh
        "http://www.mscb.com",              # Maharashtra
        "http://www.manipurscb.com",        # Manipur
        "http://www.megscb.com",            # Meghalaya
        "http://www.mizoscb.com",           # Mizoram
        "http://www.nagalandscb.com",       # Nagaland
        "http://www.oscb.org",              # Odisha
        "http://www.pscb.in",               # Punjab
        "http://www.rscb.org.in",           # Rajasthan
        "http://www.sikkimscb.com",         # Sikkim
        "http://www.tnscb.org.in",          # Tamil Nadu
        "http://www.tscab.org",             # Telangana
        "http://www.tripurascb.com",        # Tripura
        "http://www.upscb.com",             # Uttar Pradesh
        "http://www.uttaranchalscc.com",    # Uttarakhand
        "http://www.wbscb.com",             # West Bengal
        
        # State Rural Banks
        "http://www.apgvb.com",             # Andhra Pradesh Grameena Vikas Bank
        "http://www.agvbank.co.in",         # Assam Gramin Vikash Bank
        "http://www.bgvb.in",               # Bangiya Gramin Vikash Bank
        "http://www.bggb.in",               # Baroda Gujarat Gramin Bank
        "http://www.brkgb.com",             # Baroda Rajasthan Kshetriya Gramin Bank
        "http://www.cggb.co.in",            # Chhattisgarh Gramin Bank
        "http://www.dbgb.in",               # Dena Gujarat Gramin Bank
        "http://www.edb.org.in",            # Ellaquai Dehati Bank
        "http://www.hpgb.in",               # Himachal Pradesh Gramin Bank
        "http://www.jkgb.in",               # J&K Grameen Bank
        "http://www.jrgb.in",               # Jharkhand Rajya Gramin Bank
        "http://www.kvgbank.com",           # Karnataka Vikas Grameena Bank
        "http://www.keralagbank.com",       # Kerala Gramin Bank
        "http://www.mpgb.in",               # Madhyanchal Gramin Bank
        "http://www.mahagramin.in",         # Maharashtra Gramin Bank
        "http://www.mgbank.co.in",          # Manipur Rural Bank
        "http://www.meghalayarb.com",       # Meghalaya Rural Bank
        "http://www.mizoramrb.com",         # Mizoram Rural Bank
        "http://www.nagalandrb.com",        # Nagaland Rural Bank
        "http://www.odishabank.in",         # Odisha Gramya Bank
        "http://www.pbgbank.com",           # Paschim Banga Gramin Bank
        "http://www.pgb.org.in",            # Puduvai Bharathiar Grama Bank
        "http://www.punjabandsindbank.co.in", # Punjab & Sind Bank
        "http://www.rmgb.in",               # Rajasthan Marudhara Gramin Bank
        "http://www.saptagirigrameenabank.in", # Saptagiri Grameena Bank
        "http://www.sgbrrb.org",            # Sarva Haryana Gramin Bank
        "http://www.tamilnadubank.in",      # Tamil Nadu Grama Bank
        "http://www.telanganagrameenabank.com", # Telangana Grameena Bank
        "http://www.tripuragraminbank.org",  # Tripura Gramin Bank
        "http://www.ubgb.in",               # Uttar Bihar Gramin Bank
        "http://www.uttarakhandgraminbank.com" # Uttarakhand Gramin Bank
        # Major Private Sector Banks
        "https://www.hdfcbank.com",              # HDFC Bank
        "https://netbanking.hdfcbank.com",
        "https://www.icicibank.com",             # ICICI Bank
        "https://infinity.icicibank.com",
        "https://www.axisbank.com",              # Axis Bank
        "https://retail.axisbank.co.in",
        "https://www.kotak.com",                 # Kotak Mahindra Bank
        "https://netbanking.kotak.com",
        "https://www.yesbank.in",                # Yes Bank
        "https://netbanking.yesbank.co.in",
        "https://www.indusind.com",              # IndusInd Bank
        "https://indusnet.indusind.com",
        "https://www.idbibank.in",               # IDBI Bank
        "https://netbanking.idbibank.co.in",
        "https://www.rblbank.com",               # RBL Bank
        "https://inetbanking.rblbank.com",
        "https://www.bandhanbank.com",           # Bandhan Bank
        "https://netbanking.bandhanbank.com",
        "https://www.federalbank.co.in",         # Federal Bank
        "https://fednetbank.federalbank.co.in",
        "https://www.csb.co.in",                 # CSB Bank
        "https://netbanking.csb.co.in",
        "https://www.southindianbank.com",       # South Indian Bank
        "https://sibernet.southindianbank.com",
        "https://www.kvb.co.in",                 # Karur Vysya Bank
        "https://netbanking.kvb.co.in",
        "https://www.dhanbank.com",              # Dhanlaxmi Bank
        "https://netbanking.dhanbank.in",
        "https://www.tmb.in",                    # Tamilnad Mercantile Bank
        "https://netbanking.tmb.in",
        "https://www.cityunionbank.com",         # City Union Bank
        "https://www.onlinecub.net",
        "https://www.dcbbank.com",               # DCB Bank
        "https://netbanking.dcbbank.com",
        "https://www.jammuandkashmirbank.com",   # J&K Bank
        "https://netbanking.jkbank.com",
        "https://www.karnatakabank.com",         # Karnataka Bank
        "https://kbl.co.in",
        "https://www.nainitalbank.co.in",        # Nainital Bank
        "https://netbanking.nainitalbank.co.in",
        
        # Small Finance Banks
        "https://www.aubank.in",                 # AU Small Finance Bank
        "https://netbanking.aubank.in",
        "https://www.capitalbank.co.in",         # Capital Small Finance Bank
        "https://netbanking.capitalbank.co.in",
        "https://www.fincarebank.com",           # Fincare Small Finance Bank
        "https://netbanking.fincarebank.com",
        "https://www.equitasbank.com",           # Equitas Small Finance Bank
        "https://netbanking.equitasbank.com",
        "https://www.esafbank.com",              # ESAF Small Finance Bank
        "https://netbanking.esafbank.com",
        "https://www.janabank.com",              # Jana Small Finance Bank
        "https://netbanking.janabank.com",
        "https://www.nesfb.com",                 # North East Small Finance Bank
        "https://netbanking.nesfb.com",
        "https://www.suryodaybank.com",          # Suryoday Small Finance Bank
        "https://netbanking.suryodaybank.com",
        "https://www.ujjivansfb.in",             # Ujjivan Small Finance Bank
        "https://netbanking.ujjivansfb.in",
        "https://www.utkarsh.bank",              # Utkarsh Small Finance Bank
        "https://netbanking.utkarsh.bank",
        
        # Payment Banks
        "https://www.airtel.in/bank",            # Airtel Payments Bank
        "https://www.indiapost.gov.in",          # India Post Payments Bank
        "https://www.jio.com/payments-bank",     # Jio Payments Bank
        "https://www.paytmbank.com",             # Paytm Payments Bank
        "https://www.finobank.com"               # Fino Payments Bank
    ]
    
    return pd.DataFrame({"url": legitimate_urls})

def prepare_dataset():
    """
    Prepare the final dataset by combining legitimate and phishing URLs
    """
    # Get URLs
    phishing_df = download_phishing_urls()
    legitimate_df = download_legitimate_urls()
    
    # Add labels
    phishing_df['label'] = 1  # 1 for phishing
    legitimate_df['label'] = 0  # 0 for legitimate
    
    # Combine datasets
    df = pd.concat([phishing_df, legitimate_df], ignore_index=True)
    
    # Shuffle the dataset
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Save to CSV
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, 'dataset.csv')
    df.to_csv(output_path, index=False)
    
    print(f"Dataset saved to {output_path}")
    print(f"Total URLs: {len(df)}")
    print(f"Phishing URLs: {len(df[df['label'] == 1])}")
    print(f"Legitimate URLs: {len(df[df['label'] == 0])}")
    print("\nPhishing patterns used:")
    print("1. Domain name mimicking with added terms (e.g., 'secure-', '-verify')")
    print("2. Legitimate domain as subdomain of malicious domain")
    print("3. Adding security-related terms (e.g., 'secure', 'verify', 'login')")
    print("4. Using similar-looking domains with slight modifications")
    print("5. Using service-specific keywords (e.g., 'tracking', 'subscription', 'payment')")
    print("6. Multiple subdomains to obscure real domain")
    print("7. Using hyphens to separate words in domain")
    print("8. Using government domain lookalikes (e.g., 'gov.in' in different positions)")
    print("9. Using bank-specific terms (e.g., 'netbanking', 'inetbanking')")
    print("10. Using UPI and payment-related keywords")
    print("11. Using Kerala-specific service terms (e.g., 'kseb', 'ksrtc', 'kwa')")
    print("12. Using education-related keywords for university sites")
    print("13. Typosquatting variations (e.g., doubled letters, missing letters)")
    print("14. Homograph attacks using similar-looking characters")
    print("15. Mixed language patterns (English + Malayalam transliteration)")
    print("16. Emergency and time-sensitive scam patterns")
    print("17. Certificate and document verification scams")
    print("18. Job and recruitment scam patterns")
    print("19. Mobile app download scams")
    print("20. Benefit and welfare scheme scams")

if __name__ == "__main__":
    prepare_dataset()
