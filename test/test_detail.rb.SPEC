****************
Platform: X86 16bit (Intel syntax)
Code: 0x8d 0x4c 0x32 0x08 0x01 0xd8 0x81 0xc6 0x34 0x12 0x00 0x00 
Disasm:
0x1000:	lea		cx, word ptr [si + 0x32] // insn-ID: 315, insn-mnem: lea
0x1003:	or		byte ptr [bx + di], al // insn-ID: 325, insn-mnem: or
	Implicit registers modified: flags 
0x1005:	fadd		dword ptr [bx + di + 0x34c6] // insn-ID: 15, insn-mnem: fadd
	Implicit registers modified: fpsw 
0x1009:	adc		al, byte ptr [bx + si] // insn-ID: 6, insn-mnem: adc
	Implicit registers read: flags 
	Implicit registers modified: flags 
0x100b:

****************
Platform: X86 32bit (ATT syntax)
Code: 0x8d 0x4c 0x32 0x08 0x01 0xd8 0x81 0xc6 0x34 0x12 0x00 0x00 
Disasm:
0x1000:	leal		8(%edx, %esi), %ecx // insn-ID: 315, insn-mnem: lea
	This instruction belongs to groups: not64bitmode 
0x1004:	addl		%ebx, %eax // insn-ID: 8, insn-mnem: add
	Implicit registers modified: eflags 
0x1006:	addl		$0x1234, %esi // insn-ID: 8, insn-mnem: add
	Implicit registers modified: eflags 
0x100c:

****************
Platform: X86 32 (Intel syntax)
Code: 0x8d 0x4c 0x32 0x08 0x01 0xd8 0x81 0xc6 0x34 0x12 0x00 0x00 
Disasm:
0x1000:	lea		ecx, dword ptr [edx + esi + 8] // insn-ID: 315, insn-mnem: lea
	This instruction belongs to groups: not64bitmode 
0x1004:	add		eax, ebx // insn-ID: 8, insn-mnem: add
	Implicit registers modified: eflags 
0x1006:	add		esi, 0x1234 // insn-ID: 8, insn-mnem: add
	Implicit registers modified: eflags 
0x100c:

****************
Platform: X86 64 (Intel syntax)
Code: 0x55 0x48 0x8b 0x05 0xb8 0x13 0x00 0x00 
Disasm:
0x1000:	push		rbp // insn-ID: 580, insn-mnem: push
	Implicit registers read: rsp 
	Implicit registers modified: rsp 
	This instruction belongs to groups: mode64 
0x1001:	mov		rax, qword ptr [rip + 0x13b8] // insn-ID: 442, insn-mnem: mov
0x1008:

****************
Platform: ARM
Code: 0xed 0xff 0xff 0xeb 0x04 0xe0 0x2d 0xe5 0x00 0x00 0x00 0x00 0xe0 0x83 0x22 0xe5 0xf1 0x02 0x03 0x0e 0x00 0x00 0xa0 0xe3 0x02 0x30 0xc1 0xe7 0x00 0x00 0x53 0xe3 
Disasm:
0x1000:	bl		#0xfbc // insn-ID: 13, insn-mnem: bl
	Implicit registers read: pc 
	Implicit registers modified: lr 
	This instruction belongs to groups: jump arm 
0x1004:	str		lr, [sp, #-4]! // insn-ID: 212, insn-mnem: str
	This instruction belongs to groups: arm 
0x1008:	andeq		r0, r0, r0 // insn-ID: 8, insn-mnem: and
	This instruction belongs to groups: arm 
0x100c:	str		r8, [r2, #-0x3e0]! // insn-ID: 212, insn-mnem: str
	This instruction belongs to groups: arm 
0x1010:	mcreq		p2, #0, r0, c3, c1, #7 // insn-ID: 74, insn-mnem: mcr
	This instruction belongs to groups: arm 
0x1014:	mov		r0, #0 // insn-ID: 80, insn-mnem: mov
	This instruction belongs to groups: arm 
0x1018:	strb		r3, [r1, r2] // insn-ID: 203, insn-mnem: strb
	This instruction belongs to groups: arm 
0x101c:	cmp		r3, #0 // insn-ID: 23, insn-mnem: cmp
	Implicit registers modified: cpsr 
	This instruction belongs to groups: arm 
0x1020:

****************
Platform: THUMB-2
Code: 0x4f 0xf0 0x00 0x01 0xbd 0xe8 0x00 0x88 0xd1 0xe8 0x00 0xf0 
Disasm:
0x1000:	mov.w		r1, #0 // insn-ID: 80, insn-mnem: mov
	This instruction belongs to groups: thumb2 
0x1004:	pop.w		{fp, pc} // insn-ID: 425, insn-mnem: pop
	This instruction belongs to groups: thumb2 
0x1008:	tbb		[r1, r0] // insn-ID: 420, insn-mnem: tbb
	This instruction belongs to groups: thumb2 jump 
0x100c:

****************
Platform: ARM: Cortex-A15 + NEON
Code: 0x10 0xf1 0x10 0xe7 0x11 0xf2 0x31 0xe7 0xdc 0xa1 0x2e 0xf3 0xe8 0x4e 0x62 0xf3 
Disasm:
0x1000:	sdiv		r0, r0, r1 // insn-ID: 122, insn-mnem: sdiv
	This instruction belongs to groups: arm 
0x1004:	udiv		r1, r1, r2 // insn-ID: 231, insn-mnem: udiv
	This instruction belongs to groups: arm 
0x1008:	vbit		q5, q15, q6 // insn-ID: 274, insn-mnem: vbit
	This instruction belongs to groups: neon 
0x100c:	vcgt.f32		q10, q9, q12 // insn-ID: 278, insn-mnem: vcgt
	This instruction belongs to groups: neon 
0x1010:

****************
Platform: THUMB
Code: 0x70 0x47 0xeb 0x46 0x83 0xb0 0xc9 0x68 
Disasm:
0x1000:	bx		lr // insn-ID: 15, insn-mnem: bx
	This instruction belongs to groups: thumb jump 
0x1002:	mov		fp, sp // insn-ID: 80, insn-mnem: mov
	This instruction belongs to groups: thumb thumb1only 
0x1004:	sub		sp, #0xc // insn-ID: 213, insn-mnem: sub
	This instruction belongs to groups: thumb thumb1only 
0x1006:	ldr		r1, [r1, #0xc] // insn-ID: 73, insn-mnem: ldr
	This instruction belongs to groups: thumb thumb1only 
0x1008:

****************
Platform: Thumb-MClass
Code: 0xef 0xf3 0x02 0x80 
Disasm:
0x1000:	mrs		r0, eapsr // insn-ID: 87, insn-mnem: mrs
	This instruction belongs to groups: thumb mclass 
0x1004:

****************
Platform: Arm-V8
Code: 0xe0 0x3b 0xb2 0xee 0x42 0x00 0x01 0xe1 0x51 0xf0 0x7f 0xf5 
Disasm:
0x1000:	vcvtt.f64.f16		d3, s1 // insn-ID: 292, insn-mnem: vcvtt
	This instruction belongs to groups: fparmv8 dpvfp 
0x1004:	crc32b		r0, r1, r2 // insn-ID: 25, insn-mnem: crc32b
	This instruction belongs to groups: arm v8 crc 
0x1008:	dmb		oshld // insn-ID: 32, insn-mnem: dmb
	This instruction belongs to groups: arm databarrier 
0x100c:

****************
Platform: MIPS-32 (Big-endian)
Code: 0x0c 0x10 0x00 0x97 0x00 0x00 0x00 0x00 0x24 0x02 0x00 0x0c 0x8f 0xa2 0x00 0x00 0x34 0x21 0x34 0x56 0x00 0x80 0x04 0x08 
Disasm:
0x1000:	jal		0x40025c // insn-ID: 322, insn-mnem: jal
	Implicit registers modified: ra 
	This instruction belongs to groups: stdenc 
0x1004:	nop		 // insn-ID: 582, insn-mnem: nop
	This instruction belongs to groups: stdenc 
0x1008:	addiu		$v0, $zero, 0xc // insn-ID: 21, insn-mnem: addiu
	This instruction belongs to groups: stdenc 
0x100c:	lw		$v0, ($sp) // insn-ID: 353, insn-mnem: lw
	This instruction belongs to groups: stdenc 
0x1010:	ori		$at, $at, 0x3456 // insn-ID: 445, insn-mnem: ori
	This instruction belongs to groups: stdenc 
0x1014:	jr.hb		$a0 // insn-ID: 585, insn-mnem: jr.hb
	This instruction belongs to groups: stdenc mips32 notmips32r6 notmips64r6 jump 
0x1018:

****************
Platform: MIPS-64-EL (Little-endian)
Code: 0x56 0x34 0x21 0x34 0xc2 0x17 0x01 0x00 
Disasm:
0x1000:	ori		$at, $at, 0x3456 // insn-ID: 445, insn-mnem: ori
	This instruction belongs to groups: stdenc 
0x1004:	srl		$v0, $at, 0x1f // insn-ID: 525, insn-mnem: srl
	This instruction belongs to groups: stdenc 
0x1008:

****************
Platform: MIPS-32R6 | Micro (Big-endian)
Code: 0x00 0x07 0x00 0x07 0x00 0x11 0x93 0x7c 0x01 0x8c 0x8b 0x7c 0x00 0xc7 0x48 0xd0 
Disasm:
0x1000:	break		7, 0 // insn-ID: 114, insn-mnem: break
	This instruction belongs to groups: micromips 
0x1004:	wait		0x11 // insn-ID: 577, insn-mnem: wait
	This instruction belongs to groups: micromips 
0x1008:	syscall		0x18c // insn-ID: 555, insn-mnem: syscall
	This instruction belongs to groups: micromips 
0x100c:	rotrv		$t1, $a2, $a3 // insn-ID: 471, insn-mnem: rotrv
	This instruction belongs to groups: micromips 
0x1010:

****************
Platform: MIPS-32R6 (Big-endian)
Code: 0xec 0x80 0x00 0x19 0x7c 0x43 0x22 0xa0 
Disasm:
0x1000:	addiupc		$a0, 0x64 // insn-ID: 3, insn-mnem: addiupc
	This instruction belongs to groups: stdenc mips32r6 
0x1004:	align		$a0, $v0, $v1, 2 // insn-ID: 22, insn-mnem: align
	This instruction belongs to groups: stdenc mips32r6 
0x1008:

****************
Platform: ARM-64
Code: 0x09 0x00 0x38 0xd5 0xbf 0x40 0x00 0xd5 0x0c 0x05 0x13 0xd5 0x20 0x50 0x02 0x0e 0x20 0xe4 0x3d 0x0f 0x00 0x18 0xa0 0x5f 0xa2 0x00 0xae 0x9e 0x9f 0x37 0x03 0xd5 0xbf 0x33 0x03 0xd5 0xdf 0x3f 0x03 0xd5 0x21 0x7c 0x02 0x9b 0x21 0x7c 0x00 0x53 0x00 0x40 0x21 0x4b 0xe1 0x0b 0x40 0xb9 0x20 0x04 0x81 0xda 0x20 0x08 0x02 0x8b 0x10 0x5b 0xe8 0x3c 
Disasm:
0x1000:	mrs		x9, midr_el1 // insn-ID: 192, insn-mnem: mrs
0x1004:	msr		spsel, #0 // insn-ID: 193, insn-mnem: msr
	Implicit registers modified: nzcv 
0x1008:	msr		dbgdtrtx_el0, x12 // insn-ID: 193, insn-mnem: msr
0x100c:	tbx		v0.8b, {v1.16b, v2.16b, v3.16b}, v2.8b // insn-ID: 347, insn-mnem: tbx
	This instruction belongs to groups: neon 
0x1010:	scvtf		v0.2s, v1.2s, #3 // insn-ID: 234, insn-mnem: scvtf
	This instruction belongs to groups: neon 
0x1014:	fmla		s0, s0, v0.s[3] // insn-ID: 114, insn-mnem: fmla
	This instruction belongs to groups: neon 
0x1018:	fmov		x2, v5.d[1] // insn-ID: 116, insn-mnem: fmov
	This instruction belongs to groups: fparmv8 
0x101c:	dsb		nsh // insn-ID: 60, insn-mnem: dsb
0x1020:	dmb		osh // insn-ID: 58, insn-mnem: dmb
0x1024:	isb		 // insn-ID: 142, insn-mnem: isb
0x1028:	mul		x1, x1, x2 // insn-ID: 195, insn-mnem: mul
0x102c:	lsr		w1, w1, #0 // insn-ID: 184, insn-mnem: lsr
0x1030:	sub		w0, w0, w1, uxtw // insn-ID: 340, insn-mnem: sub
0x1034:	ldr		w1, [sp, #8] // insn-ID: 162, insn-mnem: ldr
0x1038:	cneg		x0, x1, ne // insn-ID: 440, insn-mnem: cneg
	Implicit registers read: nzcv 
0x103c:	add		x0, x1, x2, lsl #2 // insn-ID: 6, insn-mnem: add
0x1040:	ldr		q16, [x24, w8, uxtw #4] // insn-ID: 162, insn-mnem: ldr
0x1044:

****************
Platform: PPC-64
Code: 0x80 0x20 0x00 0x00 0x80 0x3f 0x00 0x00 0x10 0x43 0x23 0x0e 0xd0 0x44 0x00 0x80 0x4c 0x43 0x22 0x02 0x2d 0x03 0x00 0x80 0x7c 0x43 0x20 0x14 0x7c 0x43 0x20 0x93 0x4f 0x20 0x00 0x21 0x4c 0xc8 0x00 0x21 0x40 0x82 0x00 0x14 
Disasm:
0x1000:	lwz		r1, (0) // insn-ID: 347, insn-mnem: lwz
0x1004:	lwz		r1, (r31) // insn-ID: 347, insn-mnem: lwz
0x1008:	vpkpx		v2, v3, v4 // insn-ID: 570, insn-mnem: vpkpx
	This instruction belongs to groups: altivec 
0x100c:	stfs		f2, 0x80(r4) // insn-ID: 443, insn-mnem: stfs
0x1010:	crand		2, 3, 4 // insn-ID: 52, insn-mnem: crand
0x1014:	cmpwi		cr2, r3, 0x80 // insn-ID: 47, insn-mnem: cmpwi
0x1018:	addc		r2, r3, r4 // insn-ID: 2, insn-mnem: addc
	Implicit registers modified: ca 
0x101c:	mulhd.		r2, r3, r4 // insn-ID: 384, insn-mnem: mulhd
	Implicit registers modified: cr0 
0x1020:	bdnzlrl+		 // insn-ID: 28, insn-mnem: bdnzlrl
	Implicit registers read: ctr lr rm 
	Implicit registers modified: ctr 
0x1024:	bgelrl-		cr2 // insn-ID: 38, insn-mnem: blrl
	Implicit registers read: ctr lr rm 
	Implicit registers modified: lr ctr 
0x1028:	bne		0x103c // insn-ID: 13, insn-mnem: b
	Implicit registers read: ctr rm 
	Implicit registers modified: ctr 
0x102c:

****************
Platform: Sparc
Code: 0x80 0xa0 0x40 0x02 0x85 0xc2 0x60 0x08 0x85 0xe8 0x20 0x01 0x81 0xe8 0x00 0x00 0x90 0x10 0x20 0x01 0xd5 0xf6 0x10 0x16 0x21 0x00 0x00 0x0a 0x86 0x00 0x40 0x02 0x01 0x00 0x00 0x00 0x12 0xbf 0xff 0xff 0x10 0xbf 0xff 0xff 0xa0 0x02 0x00 0x09 0x0d 0xbf 0xff 0xff 0xd4 0x20 0x60 0x00 0xd4 0x4e 0x00 0x16 0x2a 0xc2 0x80 0x03 
Disasm:
0x1000:	cmp		%g1, %g2 // insn-ID: 33, insn-mnem: cmp
	Implicit registers modified: icc 
0x1004:	jmpl		%o1+8, %g2 // insn-ID: 194, insn-mnem: jmpl
0x1008:	restore		%g0, 1, %g2 // insn-ID: 226, insn-mnem: restore
0x100c:	restore		 // insn-ID: 226, insn-mnem: restore
0x1010:	mov		1, %o0 // insn-ID: 207, insn-mnem: mov
0x1014:	casx		[%i0], %l6, %o2 // insn-ID: 28, insn-mnem: casx
	This instruction belongs to groups: 64bit 
0x1018:	sethi		0xa, %l0 // insn-ID: 232, insn-mnem: sethi
0x101c:	add		%g1, %g2, %g3 // insn-ID: 6, insn-mnem: add
0x1020:	nop		 // insn-ID: 217, insn-mnem: nop
0x1024:	bne		0x1020 // insn-ID: 16, insn-mnem: b
	Implicit registers read: icc 
	This instruction belongs to groups: jump 
0x1028:	ba		0x1024 // insn-ID: 16, insn-mnem: b
	This instruction belongs to groups: jump 
0x102c:	add		%o0, %o1, %l0 // insn-ID: 6, insn-mnem: add
0x1030:	fbg		0x102c // insn-ID: 19, insn-mnem: fb
	Implicit registers read: fcc0 
	This instruction belongs to groups: jump 
0x1034:	st		%o2, [%g1] // insn-ID: 246, insn-mnem: st
0x1038:	ldsb		[%i0+%l6], %o2 // insn-ID: 198, insn-mnem: ldsb
0x103c:	brnz,a,pn		%o2, 0x1048 // insn-ID: 24, insn-mnem: brnz
	This instruction belongs to groups: 64bit jump 
0x1040:

****************
Platform: SparcV9
Code: 0x81 0xa8 0x0a 0x24 0x89 0xa0 0x10 0x20 0x89 0xa0 0x1a 0x60 0x89 0xa0 0x00 0xe0 
Disasm:
0x1000:	fcmps		%f0, %f4 // insn-ID: 70, insn-mnem: fcmps
0x1004:	fstox		%f0, %f4 // insn-ID: 181, insn-mnem: fstox
	This instruction belongs to groups: 64bit 
0x1008:	fqtoi		%f0, %f4 // insn-ID: 159, insn-mnem: fqtoi
	This instruction belongs to groups: hardquad 
0x100c:	fnegq		%f0, %f4 // insn-ID: 127, insn-mnem: fnegq
	This instruction belongs to groups: v9 
0x1010:

****************
Platform: SystemZ
Code: 0xed 0x00 0x00 0x00 0x00 0x1a 0x5a 0x0f 0x1f 0xff 0xc2 0x09 0x80 0x00 0x00 0x00 0x07 0xf7 0xeb 0x2a 0xff 0xff 0x7f 0x57 0xe3 0x01 0xff 0xff 0x7f 0x57 0xeb 0x00 0xf0 0x00 0x00 0x24 0xb2 0x4f 0x00 0x78 
Disasm:
0x1000:	adb		%f0, 0 // insn-ID: 2, insn-mnem: adb
	Implicit registers modified: cc 
0x1006:	a		%r0, 0xfff(%r15, %r1) // insn-ID: 1, insn-mnem: a
	Implicit registers modified: cc 
0x100a:	afi		%r0, -0x80000000 // insn-ID: 6, insn-mnem: afi
	Implicit registers modified: cc 
0x1010:	br		%r7 // insn-ID: 283, insn-mnem: br
	This instruction belongs to groups: jump 
0x1012:	xiy		0x7ffff(%r15), 0x2a // insn-ID: 678, insn-mnem: xiy
	Implicit registers modified: cc 
0x1018:	xy		%r0, 0x7ffff(%r1, %r15) // insn-ID: 681, insn-mnem: xy
	Implicit registers modified: cc 
0x101e:	stmg		%r0, %r0, 0(%r15) // insn-ID: 657, insn-mnem: stmg
0x1024:	ear		%r7, %a8 // insn-ID: 383, insn-mnem: ear
0x1028:

****************
Platform: XCore
Code: 0xfe 0x0f 0xfe 0x17 0x13 0x17 0xc6 0xfe 0xec 0x17 0x97 0xf8 0xec 0x4f 0x1f 0xfd 0xec 0x37 0x07 0xf2 0x45 0x5b 0xf9 0xfa 0x02 0x06 0x1b 0x10 
Disasm:
0x1000:	get		r11, ed // insn-ID: 43, insn-mnem: get
	Implicit registers modified: r11 
0x1002:	ldw		et, sp[4] // insn-ID: 66, insn-mnem: ldw
	Implicit registers read: sp 
0x1004:	setd		res[r3], r4 // insn-ID: 93, insn-mnem: setd
0x1006:	init		t[r2]:lr, r1 // insn-ID: 50, insn-mnem: init
0x100a:	divu		r9, r1, r3 // insn-ID: 26, insn-mnem: divu
0x100e:	lda16		r9, r3[-r11] // insn-ID: 62, insn-mnem: lda16
0x1012:	ldw		dp, dp[0x81c5] // insn-ID: 66, insn-mnem: ldw
0x1016:	lmul		r11, r0, r2, r5, r8, r10 // insn-ID: 68, insn-mnem: lmul
0x101a:	add		r1, r2, r3 // insn-ID: 1, insn-mnem: add
0x101c:

