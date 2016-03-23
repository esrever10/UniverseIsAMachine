class CPU:
    Opcode = {
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
    
    Register = {
        'eax'     : 0xa1,
        'ebx'     : 0xa2,
        'ecx'     : 0xa3,
        'edx'     : 0xa4,
        'esi'     : 0xa5,
        'edi'     : 0xa6,
        'ebp'     : 0xa7,
        'eesp'     : 0xa8,
        'eeip'     : 0xa9,
    }
    
    def __init__(self, vm):
        self.context = vm
        self.registers = {}
        self.opcodes = {}
        self.init_optable()
        
    def init_optable(self):
    
        self.registers = {
            CPU.Register['eax'] : 0,
            CPU.Register['ebx'] : 0,
            CPU.Register['ecx'] : 0,
            CPU.Register['edx'] : 0,
            CPU.Register['esi'] : 0,
            CPU.Register['edi'] : 0,
            CPU.Register['ebp'] : 0,
            CPU.Register['eesp'] : 0,
            CPU.Register['eeip'] : 0,
        }
        
        self.opcodes = {
            CPU.Opcode['call'] : self.v_call,
            CPU.Opcode['mov'] : self.v_mov,
            CPU.Opcode['jmp'] : self.v_jmp,
            CPU.Opcode['jz'] : self.v_jz,
            CPU.Opcode['jnz'] : self.v_jnz,
            CPU.Opcode['inc'] : self.v_inc,
            CPU.Opcode['dec'] : self.v_dec,
            CPU.Opcode['add'] : self.v_add,
            CPU.Opcode['sub'] : self.v_sub,
            CPU.Opcode['xor'] : self.v_xor,
            CPU.Opcode['cmp'] : self.v_cmp,
            CPU.Opcode['ret'] : self.v_ret,
            CPU.Opcode['read'] : self.v_read,
            CPU.Opcode['write'] : self.v_write,
            CPU.Opcode['nop'] : self.v_nop,
            CPU.Opcode['lea'] : self.v_lea,
            CPU.Opcode['push'] : self.v_push,
            CPU.Opcode['pop'] : self.v_pop,
        }
    
    @property
    def progress(self):
        return self.context.progress

    def run(self):
        self.eip = self.progress.codeseg_entry
        self.esp = 0
        while self.eip < len(self.progress.codeseg):
            opcode = self.progress.codeseg[self.eip]
            if opcode in self.opcodes.iterkeys():
                self.eip += self.opcodes[opcode]()
            else:
                self.eip += 1
           
    def v_call(self):
        print 'call'
        return 1
    
    def v_mov(self):
        print 'mov'
        return 1
    
    def v_jmp(self):
        print 'jmp'
        return 1
        
    def v_jz(self):
        print 'jz'
        return 1
    
    def v_jnz(self):
        print 'jnz'
        return 1
    
    def v_inc(self):
        print 'inc'
        return 1
        
    def v_dec(self):
        print 'dec'
        return 1
        
    def v_add(self):
        print 'add'
        return 1
    
    def v_sub(self):
        print 'sub'
        return 1
    
    def v_xor(self):
        print 'xor'
        return 1
    
    def v_cmp(self):
        print 'cmp'
        return 1
    
    def v_ret(self):
        print 'ret'
        return 1
    
    def v_read(self):
        print 'read'
        return 1
    
    def v_write(self):
        print 'write'
        return 1
    
    def v_nop(self):
        print 'nop'
        return 1
    
    def v_lea(self):
        print 'lea'
        return 1          
        
    def v_push(self):
        if self.eip + 1 >= len(self.progress.codeseg):
            print "parser error: push "
            return 1
        print 'push ' + str(self.progress.codeseg[self.eip + 1])
        
        self.progress.stack[self.esp] = self.progress.codeseg[self.eip + 1]
        self.esp += 1
        return 2
        
    def v_pop(self):
        if self.eip + 1 >= len(self.progress.codeseg):
            print "parser error: pop "
            return 1
        reg = self.progress.codeseg[self.eip + 1]
        print 'pop ' + str(reg)

        if reg in CPU.Register.iterkeys():
            self.registers[reg] = self.progress.stack[self.esp]
            self.esp -= 1
            return 2
        else:
            print "parser error: pop " + str(reg)
            return 1
        
class Progress:
    def __init__(self, program):
        self.stack = [0] * (1024 * 1024)
        self.heap = [0] * (1024 * 1024 * 5)
        self.codeseg_entry = 0
        self.codeseg = program

class VM:
    def __init__(self):
        self.cpu = CPU(self)
        self.progress = None    

    def run(self, program):
        self.progress = Progress(program)
        self.cpu.eip = self.progress.codeseg_entry
        self.cpu.run()
    
if __name__ == '__main__':
    vm = VM()
    program = range(19)
    vm.run(program)
    
    
        
    
    
    
    
    
