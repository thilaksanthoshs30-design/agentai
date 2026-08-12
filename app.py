target = f"https://www.youtube.com/results?search_query={enc}"
               msg = f"searching youtube for{q}"
     elif any(k in cmd for k in ["gmail","email","message"]):
         to, body = "",""
         clean_cmd = re.sub(
            r'^(please\s+)?(open\s+)?(gmail|email|mail|message)\s*',
            ",
            cmd
         ).strip()

         clean_cmd=re.sub(r'\b(com(and|mand)?\b','com,clean_cmd)
         parts=re.split(r'\(type|write|saying|message|content|with body)\b',clean_cmd)
         recip_part = parts[0].strip()

         recip_part=re.sub(r'^(update\s+to|to|send\s+to|and|s+update\s+to)\s*',",recip_part).strip()

         if len(parts)>1:
             body = parts[-1].strip()
         if recip_part:
             c = recip_part.replace("at", "@").replace("dot", ".").replace(" ","")
             c = re.sub(r'[^a-zA-Z0-9@,_%]',"c)
             to = c if "@" in c else f"{c}@gmail.com
         else:
              to = "thilaksanthoshs30@gmail.com
         if not body:
             body = "how was your day"
         base = "https://mail.google.com/mail/u/0?view=cm&fs=1"
         params = urllib.parse.urlencode({"to":to,"body":body})
         target = f"{base}&{params}"
         msg = f"drafting email to {to}
  else:
       enc = urllib.parse.quote_plus(cmd)
       target = f"https://www.google.com/search?q={enc}"
       msg = f"searching google for {cmd}"
  return jsonify({
         "success":True,
         "message":msg,
         "url":target
  })
 


if__name__=="__main___":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",8000))) 


