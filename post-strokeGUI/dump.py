if entry_1.get()>='0' and entry_1.get()<='1':
                            if entry_1.get()=='0': 
                                classtype3()
                            elif entry_1.get()=='1': 
                                if entry_3.get()>='2' and entry_3.get()<='4': 
                                    classtype2()
                                elif entry_3.get()=='1' or entry_3.get()=='0': 
                                    if entry_4.get()=='0' or entry_4.get()=='1': 
                                        classtype3()
                                    elif entry_4.get()>='2' and entry_4.get()<='4':
                                        classtype2()
                                    elif entry_4.get()=='':
                                        novalues()
                                    elif entry_4.get()>'4' and entry_1.get()<'0':
                                        referscore()
                                    else:
                                        furtherevaluation()
                                elif entry_3.get()=='':
                                    novalues()
                                elif entry_3.get()>'4' and entry_1.get()<'0':
                                    referscore()
                                else:
                                    furtherevaluation()
                            elif entry_1.get()=='':
                                novalues()
                            elif entry_1.get()>'4' and entry_1.get()<'0':
                                referscore()
                            else:
                                furtherevaluation()
                        elif entry_1.get()>='2' and entry_1.get()<='4': 
                            if entry_3.get()>='0' and entry_3.get()<='1':
                                if entry_1.get()<='4' and entry_1.get()>='2':
                                    if entry_2.get()>='0' and entry_2.get()<='3':
                                        if entry_4.get()=='0' or entry_4.get()=='1':
                                            if entry_1.get()=='2':
                                                classtype2()
                                            elif entry_1.get()=='3':
                                                classtype3()
                                            else:
                                                furtherevaluation()
                                        elif entry_4.get()>='2' and entry_4.get()<='4':
                                            if entry_1.get()=='2':
                                                classtype2()
                                            elif entry_1.get()=='3':
                                                classtype3()
                                            else:
                                                furtherevaluation()
                                    elif entry_2.get()>='3' and entry_2.get()<='4':
                                        if entry_4.get()=='0' or entry_4.get()=='1':
                                            if entry_1.get()<='2' and entry_2.get()>='2':
                                                classtype1()
                                            else:
                                                furtherevaluation()
                                        elif entry_4.get()>='2' and entry_4.get()<='4':
                                            if entry_1.get()=='2':
                                                classtype2()
                                            elif entry_1.get()=='3':
                                                classtype3()
                                            else:
                                                furtherevaluation()
                                elif entry_1.get()=='4':
                                    if entry_3.get()>='0' and entry_3.get()<='1':
                                        if entry_2.get()>='2' and entry_2.get()<='4':
                                            classtype2()
                                        elif entry_2.get()>='0' and entry_2.get()<='1': 
                                            classtype3()
                                        else:
                                            furtherevaluation()
                                    elif entry_3.get()>='2' and entry_3.get()<='4':
                                        if entry_2.get()>='2' and entry_2.get()<='4':
                                            classtype2()
                                        elif entry_2.get()>='0' and entry_2.get()<='1': 
                                            classtype3()
                                        else:
                                            furtherevaluation()
                            elif entry_3.get()>='2' and entry_3.get()<='4':
                                furtherevaluation()
                            elif entry_3.get()>'4' or entry_3.get()<'0':
                                referscore()
                            elif entry_3.get()=='':
                                novalues()
                        elif entry_1.get()>'4' or entry_1.get()<'0' or entry_2.get()>'4' or entry_2.get()<'0':
                            referscore()
                        elif entry_1.get()=='':
                            novalues()
                        else:
                            furtherevaluation()