class Opcode:
    call    = 0x1
    jmp     = 0x2
    jz      = 0x3
    jnz     = 0x4
    inc     = 0x5
    dec     = 0x6
    add     = 0x7
    sub     = 0x8
    xor     = 0x9
    cmp     = 0xa
    ret     = 0xb
    read    = 0xc 
    write   = 0xd
    nop     = 0xe
    lea     = 0xf
    mov     = 0x10
    push    = 0x11
    pop     = 0x12
    
class CPU:
    def __init__(self):
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.r5 = 0
        self.r6 = 0
        self.r7 = 0
        self.r8 = 0
        self.flag = 0
        self.sp = 0
        self.ip = 0
        
        
class Progress:
    def __init__(self, program):
        self.stack = []
        self.heap = []
        self.codeseg = program

class VM:
    def __init__(self):
        self.cpu = CPU()
        self.interpreter = Interpreter()
        
    def run(program):
        progress = Progress(program)
        self.cpu.ip = 0
        self.cpu.sp = 0
        self.interpreter.exec(progress)
        
class Interpreter:
    def __init__(self):
        self.table = {
            Opcode.call : self.vcall,
            Opcode.jmp : self.vjmp,
            Opcode.jz : self.vjz,
            Opcode.jnz : self.vjnz,
            Opcode.inc : self.vinc,
            Opcode.dec : self.vdec,
            Opcode.add : self.vadd,
            Opcode.sub : self.vsub,
            Opcode.xor : self.vxor,
            Opcode.cmp : self.vcmp,
            Opcode.ret : self.vret,
            Opcode.read : self.vread,
            Opcode.write : self.vwrite,
            Opcode.nop : self.vnop,
            Opcode.lea : self.vlea,
            Opcode.mov : self.vmov,
        }
    
    def exec(process):
        while self.cpu.ip < len(progress.codeseg):
            
    
    def vcall:
        
    
    def vjmp:
        
        
    def vjz:
    
    
    def vjnz:
    
    
    def vinc:
    
    
    def vdec:
    
        
    def vadd:
    
    
    def vsub:
    
    
    def vxor:
    
    
    def vcmp:
    
    
    def vret:
    
    
    def vread:
    
    
    def vwrite:
    
    
    def vnop:
    
    
    def vlea:
    
    
    def vmov:
    
    
if __name__ == '__main__':
    vm = VM()
    vm.run([])
