
class Utils:
    key = 'fw59eorpma2nvxb07liqt83_u6kgzs41-ycdjh'

    def encode_int(val):
        assert val >= 0
        out = ''
        while val > 0:
            val, digit = divmod(val, len(Utils.key))
            out += Utils.key[digit]
        return out[::-1]

    def decode_int(val):
        out = 0
        for c in val:
            out = out * len(Utils.key) + Utils.key.index(c)
        return out
