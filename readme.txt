RepuIdValidator.
    Autómata que valida el identificadores del reclusorio preventivo,
    para asegurar que complan con el formato establecido:

                REPU-2023-12345-7

    Donde:

            REPU:  Son las siglas de Reclusorio Pubico.
            2023:  Son 4 digitos que hacen alucion a un año.
            12345: Son 5 digitos que exiben la seccion del recluso.
            7:     Es el identificador del recluso.
            Separado po guiones ("-") entre secciones. 

Propiedades del autómata:
    
    Conjunto de estados:
        Q = {qe, q0, q1, q2, q3, q4, ..., q16, qf}

    Alfabeto:
        Σ={R,E,P,U,0,1,2,3,4,5,6,7,8,9,−}

    Función de transición:
        δ:Q×Σ→Q:
            δ(q0,R)=q1         δ(q0,"otro")=qe         δ(q1,E)=q2         δ(q1,"otro")=qe
            δ(q2,P)=q3         δ(q2,"otro")=qe         δ(q3,U)=q4         δ(q3,"otro")=qe
            δ(q4,-)=q5         δ(q4,"otro")=qe         δ(q5,2)=q6         δ(q5,"otro")=qe
            δ(q6,0)=q7         δ(q6,"otro")=qe         δ(q7,0-9)=q8       δ(q7,"otro")=qe
            δ(q8,0-9)=q9       δ(q8,"otro")=qe         δ(q9,-)=q10        δ(q9,"otro")=qe
            δ(q10,0-9)=q11     δ(q10,"otro")=qe        δ(q11,0-9)=q12     δ(q11,"otro")=qe
            δ(q12,0-9)=q13     δ(q12,"otro")=qe        δ(q13,0-9)=q14     δ(q13,"otro")=qe
            δ(q14,0-9)=q15     δ(q14,"otro")=qe        δ(q15,-)=q16       δ(q15,"otro")=qe
            δ(q16,0-9)=qf      δ(q16,"otro")=qe

            q0 = Estado Incial
            qf = Estado Final
            qe = Estado de error