func backspaceCompare(s string, t string) bool {
    sn := len(s)
    tn := len(t)
    i:=sn-1
    j:=tn-1
    sb, tb := 0, 0
    for  i >=0 || j>=0{
        if i >=0{
            if s[i] == '#'{
                sb++
                i--
            }else{
                //letter
                if sb > 0{
                    i--
                    sb--
                    continue
                }else{
                    //for t empty
                    if j < 0 {return false}
                }
            }
        }
        if j >=0{
            if t[j] == '#'{
                tb++
                j--
            }else{
                //letter
                if tb > 0{
                    j--
                    tb--
                    continue
                }else{
                    //for s empty
                    if i < 0 {return false}
                }
            }
        }

        //fmt.Println(i, " ", j, " ", tb)
        
        if sb == 0 && tb==0{

            if i >=0 && j>=0 {
                if s[i] != t [j] { 
                    return false
                }
                i--
                j--
            }
        }    
    } 
    return true
}