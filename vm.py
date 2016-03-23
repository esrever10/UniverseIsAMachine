class CPU:
    Opcodes = {
        'call'    : 0x1,
        'mov'     : 0x2,
        'jmp'     : 0x3,
        'jz'      : 0x4,
        'jnz'     : 0x5,
        'inc'     : 0x6,
        'dec'     : 0x7,
        'add'     : 0x8,
        'sub'     : 0x9,
        'xor'     : 0xa,
        'cmp'     : 0xb,
        'ret'     : 0xc,
        'read'    : 0xd, 
        'write'   : 0xe,
        'nop'     : 0xf,
        'lea'     : 0x10,
        'push'    : 0x11,
        'pop'     : 0x12,
    }
    
    def __init__(self, vm):
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.r5 = 0
        self.r6 = 0
        self.r7 = 0
        self.r8 = 0
        self.sp = 0
        self.ip = 0
        self.flag = 0
        self.context = vm
        self.optable = {}
        self.init_optable()
    
    def init_optable(self):
        self.optable = {
            CPU.Opcodes['call'] : self.v_call,
            CPU.Opcodes['mov'] : self.v_mov,
            CPU.Opcodes['jmp'] : self.v_jmp,
            CPU.Opcodes['jz'] : self.v_jz,
            CPU.Opcodes['jnz'] : self.v_jnz,
            CPU.Opcodes['inc'] : self.v_inc,
            CPU.Opcodes['dec'] : self.v_dec,
            CPU.Opcodes['add'] : self.v_add,
            CPU.Opcodes['sub'] : self.v_sub,
            CPU.Opcodes['xor'] : self.v_xor,
            CPU.Opcodes['cmp'] : self.v_cmp,
            CPU.Opcodes['ret'] : self.v_ret,
            CPU.Opcodes['read'] : self.v_read,
            CPU.Opcodes['write'] : self.v_write,
            CPU.Opcodes['nop'] : self.v_nop,
            CPU.Opcodes['lea'] : self.v_lea,
            CPU.Opcodes['push'] : self.v_push,
            CPU.Opcodes['pop'] : self.v_pop,
        }
    
    def run(self, progress):
        self.ip = 0
        self.sp = 0
        while self.ip < len(progress.codeseg):
            op = progress.codeseg[self.ip]
            if op in self.optable.iterkeys():
                self.optable[op]()
            else:
                self.ip += 1
                  
    def v_call(self):
        print 'call'
        self.ip += 1
    
    def v_mov(self):
        print 'mov'
        self.ip += 1
    
    def v_jmp(self):
        print 'jmp'
        self.ip += 1
        
    def v_jz(self):
        print 'jz'
        self.ip += 1
    
    def v_jnz(self):
        print 'jnz'
        self.ip += 1
    
    def v_inc(self):
        print 'inc'
        self.ip += 1
        
    def v_dec(self):
        print 'dec'
        self.ip += 1
        
    def v_add(self):
        print 'add'
        self.ip += 1
    
    def v_sub(self):
        print 'sub'
        self.ip += 1
    
    def v_xor(self):
        print 'xor'
        self.ip += 1
    
    def v_cmp(self):
        print 'cmp'
        self.ip += 1
    
    def v_ret(self):
        print 'ret'
        self.ip += 1
    
    def v_read(self):
        print 'read'
        self.ip += 1
    
    def v_write(self):
        print 'write'
        self.ip += 1
    
    def v_nop(self):
        print 'nop'
        self.ip += 1
    
    def v_lea(self):
        print 'lea'
        self.ip += 1           
        
    def v_push(self):
        print 'push'
        self.ip += 1
        
    def v_pop(self):
        print 'pop'
        self.ip += 1    
        
class Progress:
    def __init__(self, program):
        self.stack = []
        self.heap = []
        self.codeseg = program

class VM:
    def __init__(self):
        self.cpu = CPU(self)

    def run(self, program):
        progress = Progress(program)
        self.cpu.run(progress)
    
if __name__ == '__main__':
    vm = VM()
    program = range(19)
    vm.run(program)
    
    
        
    
    
    
    
    
