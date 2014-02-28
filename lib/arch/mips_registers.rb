module Crabstone
  module MIPS
    REG_LOOKUP= {
      "INVALID" => 0,
      "0" => 1,
      "1" => 2,
      "2" => 3,
      "3" => 4,
      "4" => 5,
      "5" => 6,
      "6" => 7,
      "7" => 8,
      "8" => 9,
      "9" => 10,
      "10" => 11,
      "11" => 12,
      "12" => 13,
      "13" => 14,
      "14" => 15,
      "15" => 16,
      "16" => 17,
      "17" => 18,
      "18" => 19,
      "19" => 20,
      "20" => 21,
      "21" => 22,
      "22" => 23,
      "23" => 24,
      "24" => 25,
      "25" => 26,
      "26" => 27,
      "27" => 28,
      "28" => 29,
      "29" => 30,
      "30" => 31,
      "31" => 32,
      "DSPCCOND" => 33,
      "DSPCARRY" => 34,
      "DSPEFI" => 35,
      "DSPOUTFLAG" => 36,
      "DSPOUTFLAG16_19" => 37,
      "DSPOUTFLAG20" => 38,
      "DSPOUTFLAG21" => 39,
      "DSPOUTFLAG22" => 40,
      "DSPOUTFLAG23" => 41,
      "DSPPOS" => 42,
      "DSPSCOUNT" => 43,
      "AC0" => 44,
      "AC1" => 45,
      "AC2" => 46,
      "AC3" => 47,
      "F0" => 48,
      "F1" => 49,
      "F2" => 50,
      "F3" => 51,
      "F4" => 52,
      "F5" => 53,
      "F6" => 54,
      "F7" => 55,
      "F8" => 56,
      "F9" => 57,
      "F10" => 58,
      "F11" => 59,
      "F12" => 60,
      "F13" => 61,
      "F14" => 62,
      "F15" => 63,
      "F16" => 64,
      "F17" => 65,
      "F18" => 66,
      "F19" => 67,
      "F20" => 68,
      "F21" => 69,
      "F22" => 70,
      "F23" => 71,
      "F24" => 72,
      "F25" => 73,
      "F26" => 74,
      "F27" => 75,
      "F28" => 76,
      "F29" => 77,
      "F30" => 78,
      "F31" => 79,
      "FCC0" => 80,
      "FCC1" => 81,
      "FCC2" => 82,
      "FCC3" => 83,
      "FCC4" => 84,
      "FCC5" => 85,
      "FCC6" => 86,
      "FCC7" => 87,
      "W0" => 88,
      "W1" => 89,
      "W2" => 90,
      "W3" => 91,
      "W4" => 92,
      "W5" => 93,
      "W6" => 94,
      "W7" => 95,
      "W8" => 96,
      "W9" => 97,
      "W10" => 98,
      "W11" => 99,
      "W12" => 100,
      "W13" => 101,
      "W14" => 102,
      "W15" => 103,
      "W16" => 104,
      "W17" => 105,
      "W18" => 106,
      "W19" => 107,
      "W20" => 108,
      "W21" => 109,
      "W22" => 110,
      "W23" => 111,
      "W24" => 112,
      "W25" => 113,
      "W26" => 114,
      "W27" => 115,
      "W28" => 116,
      "W29" => 117,
      "W30" => 118,
      "W31" => 119,
      "HI" => 120,
      "LO" => 121,
      "PC" => 122,
      "ZERO" => 1,
      "AT" => 2,
      "V0" => 3,
      "V1" => 4,
      "A0" => 5,
      "A1" => 6,
      "A2" => 7,
      "A3" => 8,
      "T0" => 9,
      "T1" => 10,
      "T2" => 11,
      "T3" => 12,
      "T4" => 13,
      "T5" => 14,
      "T6" => 15,
      "T7" => 16,
      "S0" => 17,
      "S1" => 18,
      "S2" => 19,
      "S3" => 20,
      "S4" => 21,
      "S5" => 22,
      "S6" => 23,
      "S7" => 24,
      "T8" => 25,
      "T9" => 26,
      "K0" => 27,
      "K1" => 28,
      "GP" => 29,
      "SP" => 30,
      "FP" => 31,
      "S8" => 31,
      "RA" => 32,
      "HI0" => 44,
      "HI1" => 45,
      "HI2" => 46,
      "HI3" => 47,
      "LO0" => 44,
      "LO1" => 45,
      "LO2" => 46,
      "LO3" => 47
    }
    ID_LOOKUP = REG_LOOKUP.invert
    SYM_LOOKUP = Hash[REG_LOOKUP.map {|k,v| [k.downcase.to_sym,v]}]

    def self.register reg
      return reg if ID_LOOKUP[reg]
      return SYM_LOOKUP[reg] if SYM_LOOKUP[reg]
      if reg.respond_to? :upcase
        return REG_LOOKUP[reg.upcase] || REG_LOOKUP['INVALID']
      end
      REG_LOOKUP['INVALID']
    end

  end
end
