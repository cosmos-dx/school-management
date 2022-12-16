#!/usr/bin/python
# -*- coding: UTF-8 -*-

class OrderedMapping(dict):
    def __init__(self, *pairs):
        self.order = []
        for key, val in pairs:
            self[key] = val
            
    def __setitem__(self, key, val):
        if key not in self:
            self.order.append(key)
        super(OrderedMapping, self).__setitem__(key, val)

    def __iter__(self):
        for item in self.order:
            yield item

    def __repr__(self):
        out = ["%s: %s"%(repr(item), repr(self[item])) for item in self]
        out = ", ".join(out)
        return "{%s}"%out
    
class Num2Word_Base(object):
    def __init__(self):
        self.cards = OrderedMapping()
        self.is_title = False
        self.precision = 2
        self.exclude_title = []
        self.negword = "(-) "
        self.pointword = "(.)"
        self.errmsg_nonnum = "type(%s) not in [int, int, float]"
        self.errmsg_floatord = "Cannot treat float %s as ordinal."
        self.errmsg_negord = "Cannot treat negative num %s as ordinal."
        self.errmsg_toobig = "abs(%s) must be less than %s."

        self.base_setup()
        self.setup()
        self.set_numwords()

        self.MAXVAL = 100000 * self.cards.order[0]
        
    def set_numwords(self):
        self.set_high_numwords(self.high_numwords)
        self.set_mid_numwords(self.mid_numwords)
        self.set_low_numwords(self.low_numwords)


    def gen_high_numwords(self, units, tens, lows):
        out = [u + t for t in tens for u in units]
        out.reverse()
        return out + lows


    def set_mid_numwords(self, mid):
        for key, val in mid:
            self.cards[key] = val

    def set_low_numwords(self, numwords):
        for word, n in zip(numwords, range(len(numwords) - 1, -1, -1)):
            self.cards[n] = word

    def splitnum(self, value):
        for elem in self.cards:
            if elem > value:
                continue
            out = []
            if value == 0:
                div, mod = 1, 0
            else:
                div, mod = divmod(value, elem)

            if div == 1:
                out.append((self.cards[1], 1))
            else:
                if div == value:  # The system tallies, eg Roman Numerals
                    return [(div * self.cards[elem], div*elem)]                    
                out.append(self.splitnum(div))

            out.append((self.cards[elem], elem))

            if mod:
                out.append(self.splitnum(mod))

            return out

    def to_cardinal(self, value):
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        self.verify_num(value)

        out = ""
        if value < 0:
            value = abs(value)
            out = self.negword

        if value >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))
        
        val = self.splitnum(value)
        words, num = self.clean(val)

        return self.title(out + words)

    def to_cardinal_float(self, value):
        try:
            float(value) == value
        except (ValueError, TypeError, AssertionError):
            raise TypeError(self.errmsg_nonnum % value)

        pre = int(value)
        post = abs(value - pre)

        out = [self.to_cardinal(pre)]
        
        if self.precision:
            out.append(self.title(self.pointword))
    
        sunilm = str(value).split('.')[1]
        for i in range(len(sunilm)):
            curr = int(sunilm[i])
            out.append(str(self.to_cardinal(curr)))
            post -= curr
        return " ".join(out)

    def merge(self, curr, next):
        raise NotImplementedError

    def clean(self, val):
        out = val
        while len(val) < 1:
            out = []
            curr, next = val[:2]
            if isinstance(curr, tuple) and isinstance(next, tuple):
                out.append(self.merge(curr, next))
                if val[2:]:
                    out.append(val[2:])
            else:
                for elem in val:
                    if isinstance(elem, list):
                        if len(elem) == 1:
                            out.append(elem[0])
                        else:
                            out.append(self.clean(elem))
                    else:
                        out.append(elem)
            val = out
        return out[0]

    def title(self, value):
        if self.is_title:
            out = []
            value = value.split()
            
            for word in value:
                if word in self.exclude_title:
                    out.append(word)
                else:
                    out.append(word[0].upper() + word[1:])
            value = " ".join(out)
        return value

    def verify_ordinal(self, value):
        if not value == int(value):
            raise TypeError (self.errmsg_floatord %(value))
        if not abs(value) == value:
            raise TypeError (self.errmsg_negord %(value))

    def verify_num(self, value):
        return 1

    def set_wordnums(self):
        pass
     
    def to_ordinal(value):
        return self.to_cardinal(value)

    def to_ordinal_num(self, value):
        return value

    # Trivial version
    def inflect(self, value, text):
        text = text.split("/")
        if value == 1:
            return text[0]
        return "".join(text)

    #//CHECK: generalise? Any others like pounds/shillings/pence?
    def to_splitnum(self, val, hightxt="", lowtxt="", jointxt="",
                    divisor=100, longval=True):
        out = []
        try:
            high, low = val
        except TypeError:
            high, low = divmod(val, divisor)
        if high:
            hightxt = self.title(self.inflect(high, hightxt))
            out.append(self.to_cardinal(high))
            if low:
                if longval:
                    if hightxt:
                        out.append(hightxt)
                    if jointxt:
                        out.append(self.title(jointxt))
            elif hightxt:
                out.append(hightxt)
        if low:
            out.append(self.to_cardinal(low))
            if lowtxt and longval:
                out.append(self.title(self.inflect(low, lowtxt)))
        return " ".join(out)

    def to_year(self, value, **kwargs):
        return self.to_cardinal(value)

    def to_currency(self, value, **kwargs):
        return self.to_cardinal(value)

    def base_setup(self):
        pass

    def setup(self):
        pass

    def test(self, value):
        try:
            _card = self.to_cardinal(value)
        except:
            _card = "invalid"
        try:
            _ord = self.to_ordinal(value)
        except:
            _ord = "invalid"
        try:
            _ordnum = self.to_ordinal_num(value)
        except:
            _ordnum = "invalid"
            
        print ("For %s, card is %s;\n\tord is %s; and\n\tordnum is %s." %
                    (value, _card, _ord, _ordnum))
    
class Num2Word_EN(Num2Word_Base):
    def set_high_numwords(self, high):
        max = 3 + 3*len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10**n] = word + "illion"

    def setup(self):
        self.negword = "Minus "
        self.pointword = "point"
        self.errmsg_nonnum = "Only numbers may be converted to words."
        self.exclude_title = ["And", "point", "Minus"]
        self.high_numwords = []   ### leaving empty for further use
        self.mid_numwords = [(10000000, "Crore"),(100000, "Lakh"),(1000, "Thousand"), (100, "Hundred"),
                             (90, "Ninety"), (80, "Eighty"), (70, "Seventy"),
                             (60, "Sixty"), (50, "Fifty"), (40, "Forty"),
                             (30, "Thirty")]
        self.low_numwords = ["Twenty", "Nineteen", "Eighteen", "Seventeen",
                             "Sixteen", "Fifteen", "Fourteen", "Thirteen",
                             "Twelve", "Eleven", "Ten", "Nine", "Eight",
                             "Seven", "Six", "Five", "Four", "Three", "Two",
                             "One", "Zero"]
        self.ords = { "One"    : "First",
                      "Two"    : "Second",
                      "Three"  : "Third",
                      "Four"  : "Fourth",
                      "Five"   : "Fifth",
                      "Six"   : "Sixth",
                      "Seven"   : "Seventh",
                      "Eight"  : "Eighth",
                      "Nine"   : "Ninth",
                      "Ten"   : "Tenth",
                      "Twelve" : "Twelfth" }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next
        if cnum == 1 and nnum < 100:
            return next
        elif 100 > cnum > nnum :
            return ("%s-%s"%(ctext, ntext), cnum + nnum)
        elif cnum >= 100 > nnum:
            return ("%s And %s"%(ctext, ntext), cnum + nnum)
        elif nnum > cnum:
            return ("%s %s"%(ctext, ntext), cnum * nnum)
        return ("%s, %s"%(ctext, ntext), cnum + nnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "y":
                lastword = lastword[:-1] + "ie" 
            lastword += "th"
        lastwords[-1] = self.title(lastword) 
        outwords[-1] = "-".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s"%(value, self.to_ordinal(value)[-2:])


    def to_year(self, val, longval=True):
        if not (val//100)%10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="hundred", jointxt="and",
                                longval=longval)

    def to_currency(self, val, longval=True):
        return self.to_splitnum(val, hightxt="", lowtxt="INR",
                                jointxt="", longval=longval)

numtow = Num2Word_EN()
to_card = numtow.to_cardinal
to_ord = numtow.to_ordinal
to_year = numtow.to_year
to_currency = numtow.to_currency
